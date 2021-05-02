import win32api
import win32file
import pywintypes
import winerror
import win32event
import win32con
import ntsecuritycon
import sys
import os
import tempfile
import threading
import time
import shutil
from shutil import copyfile

class StoppableFolderReplicator(): 

    def __init__(self, srcFolder, destFolder, hEvent):
        self.srcFolder = srcFolder
        self.destFolder = destFolder
        self.hEvent = hEvent
        self.tearDownInProgress = False

        self.ACTIONS = {
                1 : "Created",
                2 : "Deleted",
                3 : "Updated",
                4 : "Renamed from something",
                5 : "Renamed to something"
            }
        
        self.dir_handle = win32file.CreateFile(srcFolder, 
                                        ntsecuritycon.FILE_LIST_DIRECTORY,
                                        win32con.FILE_SHARE_READ,
                                        None, # security desc
                                        win32con.OPEN_EXISTING,
                                        win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED,
                                        None)

        self.watcher_thread = threading.Thread(target=self._watcherThreadOverlapped,
                            args=(srcFolder, destFolder, self.dir_handle))
        self.watcher_thread.start()


    def _watcherThreadOverlapped(self, srcFolder, destFolder, dir_handle):
        print("thread #2:waiting for directory changes")
        changes = []
        flags = win32con.FILE_NOTIFY_CHANGE_FILE_NAME
        buf = win32file.AllocateReadBuffer(8192)
        overlapped = pywintypes.OVERLAPPED()
        overlapped.hEvent = win32event.CreateEvent(None, 0, 0, None)
        while 1:
            if self.tearDownInProgress:
                print("thread #2:tidying up")
                if self.dir_handle != 0:
                    win32api.CloseHandle(self.dir_handle)
                    self.dir_handle = 0
                break
            try:
                win32file.ReadDirectoryChangesW(self.dir_handle,
                                                buf,
                                                False, #sub-tree
                                                flags,
                                                overlapped)
            except Exception as e:
                print("thread #2: Exception whilst ReadDirectoryChangesW:" + str(e) + "\n")
                break 
            # Wait for our event or for a short time.
            rc = win32event.WaitForSingleObject(overlapped.hEvent, 1000)
            if rc == win32event.WAIT_OBJECT_0:
                # got some data!  Must use GetOverlappedResult to find out
                # how much is valid!  0 generally means the handle has
                # been closed.  Blocking is OK here, as the event has
                # already been set.
                nbytes = win32file.GetOverlappedResult(dir_handle, overlapped, True)
                if nbytes:
                    bits = win32file.FILE_NOTIFY_INFORMATION(buf, nbytes)
                    changes.extend(bits)

                    for action, file in changes:
                        full_filename = os.path.join(srcFolder, file)
                        print("thread #2:" , full_filename, self.ACTIONS.get(action, "Unknown"))
                        if action == 1 or action == 3:
                            #
                            # perhaps put some filtering or file renaming logic
                            # in here
                            #
                            if os.path.isfile(full_filename):
                                sDestFilename = os.path.join(destFolder, file)
                                try:
                                    copyfile(full_filename,sDestFilename)
                                except Exception as e:
                                    print("thread #2: Exception whilst copying file '" + full_filename + "':" + str(e) + "\n")
                    changes = []  # bugfix, need to clear this other it accumulates
                else:
                    # This is "normal" exit - our 'tearDown' closes the
                    # handle.
                    # print "looks like dir handle was closed!"
                    break
        print ("thread #2:stopped")

    def waitForEvent(self):
        try:
            print("thread #1:waiting for stop event")
            while 1:
                
                dwWaitResult = win32event.WaitForSingleObject(self.hEvent.handle, 500)
                if dwWaitResult == win32event.WAIT_OBJECT_0:
                    print("thread #1:stop signal received...")
                    self.tearDownInProgress = True
                    self.watcher_thread.join(5)
                    return
                pass

        except Exception as e:
            print("thread #1:Exception whilst polling for event:'" + self.stopEventName + "':" + str(e) + "\n")

        
if __name__ == '__main__':

    if len(sys.argv) < 4:
        print("Usage:" + os.path.basename(__file__) + " <sourceFolder> <destinationFolder> <stopEventName>")
    else:
        srcFolder = sys.argv[1]
        destFolder = sys.argv[2]
        stopEventName = sys.argv[3]

        ok = True
        if not os.path.isdir(srcFolder):
            print("Error, srcFolder '" + srcFolder + "' does not exist!  Abandoning.")
            ok = False

        if not os.path.isdir(destFolder):
            print("Error, destFolder '" + destFolder + "' does not exist!  Abandoning.")
            ok = False

        if ok == True:
            try:
                stoppable = False
                hEvent = win32event.OpenEvent(ntsecuritycon.SYNCHRONIZE, 0, stopEventName)
                
                stoppable = True
            except Exception as e:
                print("Exception whilst opening event:'" + stopEventName + "':" + str(e) + "\n")

            if stoppable:
                foo = StoppableFolderReplicator(srcFolder, destFolder, hEvent) 
                foo.waitForEvent()
                win32api.CloseHandle(hEvent)
                print("all stopped")
            else:
                print("Not stoppable, abandoning!")
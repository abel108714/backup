Imports System.IO
Imports System.Threading
Imports System.Runtime.InteropServices

Public Class Form1

    Private WithEvents kbHook As New KeyboardHook

    Private Declare Function BlockInput Lib "user32" _
        (ByVal fBlock As Integer) As Integer
    Declare Auto Function SetCursorPos Lib "user32" (ByVal x As Integer, ByVal y As Integer) As Integer
    Declare Sub mouse_event Lib "user32" (ByVal dwFlags As Integer, ByVal dx As Integer, ByVal dy As Integer, ByVal dwData As Integer, ByVal dwExtraInfo As Integer)

    Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Integer
    Declare Function FindWindowEx Lib "user32" Alias "FindWindowExA" _
    (ByVal hWndParent As Integer, ByVal hWndChildAfter As Integer, ByVal lpClassName As String, ByVal lpWindowName As String) As Integer
    Private Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As IntPtr) As Long

    Public Const MOUSEEVENTF_LEFTDOWN = &H2
    Public Const MOUSEEVENTF_LEFTUP = &H4
    Public Const MOUSEEVENTF_MIDDLEDOWN = &H20
    Public Const MOUSEEVENTF_MIDDLEUP = &H40
    Public Const MOUSEEVENTF_RIGHTDOWN = &H8
    Public Const MOUSEEVENTF_RIGHTUP = &H10
    Public Const MOUSEEVENTF_MOVE = &H1
    Dim a As New Process

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        Dim debug As Integer = 0
        Me.Show()
        'Me.Show()

        'Me.Hide()
        'Me.Visible = False

        Dim hwd As IntPtr
        'Dim hwd1 As IntPtr
        'Label1.Text = "產生報表中，勿移動滑鼠及操控鍵盤"
        'Label2.Text = "F1關閉"
        'Label1.Refresh()
        'Label2.Refresh()
        'Me.Show()
        Dim NowDate As String = System.DateTime.Now
        Dim EarMonDate As String = DateTime.Parse(NowDate).ToString("yyy/MM/") & "01"
        Dim StartDate As String = DateTime.Parse(System.DateTime.Now).ToString("yyyyMM") & "01"
        NowDate = DateTime.Parse(NowDate).ToString("yyy/MM/dd")
        NowDate = DateTime.Parse(NowDate).ToString("yyyyMMdd")


        Dim EndDate As String
        'MsgBox(NowDate)
        a.StartInfo.FileName = "C:\Conductor\C_dsbin\MainMenu.exe"
        a.Start()


        hwd = FindWindow(vbNullString, "鼎新電腦 Cosmos ERP")
        If hwd.Equals(IntPtr.Zero) Then '若已開啟就不等待秒數
            Thread.Sleep(13000)
        Else
            Thread.Sleep(3000)
        End If

        setSendKeys("01439{enter}", 10)
        'setSendTab(3, 1) '到輸入代號位置
        SetCursorPos(100, 175) '到輸入代號位置100,175
        setMouseClick("left", 2)
        SendKeys.SendWait("POSI49{enter}") 'SendKeys.SendWait("COPR38{enter}") '輸入代號

        Thread.Sleep(10 * 1000)
        'hwd = FindWindow(vbNullString, "交易明細資訊維護作業")
        'hwd = FindWindow(vbNullString, "交易明細資訊維護作業(POSI49)")
        'LeaderWorkCenter.exe
        'Dim p() As Process = System.Diagnostics.Process.GetProcessesByName("LeaderWorkCenter.exe")
        'hwd1 = p(0).MainWindowHandle
        'SetForegroundWindow(hwd1)
        'MsgBox("1234")
        setSendTab(1, 5)
        Thread.Sleep(10 * 1000)


        Dim NewPos As ScrnPt = New ScrnPt(1280, 1024, 1366, 768)


        SetCursorPos(NewPos.getPosX(619), NewPos.getPosY(198)) '619, 198 按視窗'619,77(新螢幕)
        'SetCursorPos(703, 533) '703,533 按視窗　

        'debug += 1
        setMouseClick("left", 2)
        'debug += 1
        SendKeys.SendWait("%(D)")
        'debug += 1
        SendKeys.SendWait("{Q}")

        'debug += 1
        SetCursorPos(NewPos.getPosX(525), NewPos.getPosY(329)) '525,329 按進階設定'617,70(新螢幕)
        'debug += 1
        setMouseClick("left", 2)
        'debug += 1
        SetCursorPos(NewPos.getPosX(645), NewPos.getPosY(486)) '645,486
        'debug += 1
        setMouseClick("left", 2)

        'SetCursorPos(600, 475) '600, 475
        'setMouseClick("left", 2)



        '(POSTA.TA001 >= N'20200801')
        'And (POSTA.TA038 = N'4')

        '(POSTB.TB010 = N'11704121')
        'And (POSTB.TB018 = 1750)
        'And (POSTB.TB013 = N'11704121')
        'And (POSTB.TB009 = N'4719349110337')

        'NowDate = "20200901"
        Dim cmd_test As Cmd = New Cmd()
        'debug += 1
        'cmd_test.cmd("echo " & debug & "> t.txt")

        'debug += 1
        'cmd_test.cmd("echo " & debug & "> t.txt")

        'StartDate = DateTime.Parse(NowDate).ToString("yyyyMM") & "01" '"20200801" '測試用日期
        'debug += 1
        'cmd_test.cmd("echo " & debug & "> t.txt")
        EndDate = NowDate '"20200831"
        'debug += 1
        'cmd_test.cmd("echo " & debug & "> t.txt")
        SendKeys.SendWait("{(}POSTA.TA001 >= N'" & StartDate & "'{)} And {(}POSTA.TA001 <= N'" & EndDate & "'{)}") 'And {(}POSTA.TA038 = N'4'{)} '(POSTA.TA001 = N'20200806')設定查詢條件
        'SendKeys.SendWait("{(}POSTA.TA001 >= N'20200801'{)} And {(}POSTA.TA001 <= N'20200831'{)}")

        'debug += 1
        'cmd_test.cmd("echo " & debug & "> t.txt")
        '(POSTA.TA001 >= N'20200801') And (POSTA.TA001 <= N'20200831') And (POSTA.TA038 = N'4') And (POSTA.TA038 = N'5')"
        Thread.Sleep(10 * 1000)
        SetCursorPos(NewPos.getPosX(498), NewPos.getPosY(546)) '498,546 按單身
        setMouseClick("left", 2)
        SetCursorPos(NewPos.getPosX(645), NewPos.getPosY(486)) '645,486
        setMouseClick("left", 2)
        Thread.Sleep(10 * 1000)
        SendKeys.SendWait("{(}POSTB.TB010 = N'11704121'{)} And {(}POSTB.TB018 = 1750{)} And {(}POSTB.TB013 = N'11704121'{)} And {(}POSTB.TB009 = N'4719349110337'{)}") '(POSTB.TB010 = N'11704121')    '643,599
        '(POSTB.TB010 = N'11704121') And (POSTB.TB018 = 1750) And (POSTB.TB013 = N'11704121') And (POSTB.TB009 = N'4719349110337')
        Thread.Sleep(10 * 1000)
        SetCursorPos(NewPos.getPosX(504), NewPos.getPosY(742)) '504, 742 按按確定
        setMouseClick("left", 2)



        '------------------
        '先取得頁籤要按幾次
        '------------------
        Thread.Sleep(10 * 1000)
        SetCursorPos(NewPos.getPosX(544), NewPos.getPosY(250)) '544, 250 按轉出excel
        setMouseClick("left", 2)

        SetCursorPos(NewPos.getPosX(516), NewPos.getPosY(730)) '516,730 按確定
        setMouseClick("left", 2)
        Thread.Sleep(10 * 1000)
        setSendKeys("{RIGHT}", 1) '按右,不開excel
        setSendEnter(0)

        '打開檔案，啟動巨集計算列數寫入txt檔，然後關閉且刪除檔案
        Dim DataCt As String
        Dim fileReader As String
        Dim docpath As String = "C:" & Environ("HOMEPATH") & "\Documents"
        Dim mydocpath As String = "C:\MyDocu~1" 'My Documents
        Dim xlApp_macro As Object
        Dim xlBook_macro As Object
        Dim xlBook As Object
        Dim xlsheet As Object
        Dim MacroPath As String = "S:\網通部\◎資訊\data\績效資料\"
        Dim SouPath As String = "C:\Users\udev77\Documents\COSMOS_ERP\C_Data\"


        'MsgBox(1)
        'MsgBox(SouPath & Convert.ToString("POSI49_1.XLSX"))
        If File.Exists(SouPath & Convert.ToString("POSI49_1.XLSX")) Then '如果有預購資料
            'MsgBox(2)
            cmd_test.cmd("taskkill /f /im excel.exe")
            xlApp_macro = CreateObject("Excel.Application") '創建EXCEL應用類
            xlApp_macro.Visible = True '設置EXCEL可見
            'S:\網通部\◎資訊\data\績效資料\book1.xlsm
            'C:\Users\udev77\Documents\COSMOS_ERP\C_Data\POSI49_1.XLSX
            xlBook_macro = xlApp_macro.Workbooks.Open(MacroPath & "book1.xlsm") '打開EXCEL工作簿
            'MsgBox("1")
            'debug += 1
            xlBook = xlApp_macro.Workbooks.Open(SouPath & "POSI49_1.XLSX") '打開EXCEL工作簿
            'MsgBox("2")
            'debug += 1
            xlsheet = xlBook.Worksheets(1) '打開EXCEL第二頁工作表
            'MsgBox("3")
            'debug += 1
            xlsheet.Activate '啟動第一頁工作表
            'MsgBox("4")
            'debug += 1
            xlApp_macro.Run("'Book1.xlsm'!setDataCt") '記錄資料列數寫入到DataCt.txt
            'MsgBox("5")
            'debug += 1
            'xlsheet = xlBook.Worksheets(2) '打開EXCEL第二頁工作表
            'xlsheet.Activate '啟動第二頁工作表
            xlApp_macro = Nothing '釋放EXCEL對象
            'MsgBox("6")
            'debug += 1
            cmd_test.cmd("taskkill /f /im excel.exe")
            'MsgBox("7")
            'debug += 1
            cmd_test.cmd("del C:\Users\udev77\Documents\COSMOS_ERP\C_Data\POSI49_1.XLSX")
            'MsgBox("8")
            'debug += 1



            '讀取記錄及檢查檔案是否存在
            'Environ("HOMEPATH") 
            'OutputFilePath = "C:" & Environ("HOMEPATH") & "\Documents\DataCt.txt"
            If File.Exists(docpath & Convert.ToString("\DataCt.txt")) Then
                'MsgBox("檔案存在")
                fileReader = My.Computer.FileSystem.ReadAllText(docpath & Convert.ToString("\DataCt.txt"), System.Text.Encoding.UTF8)
                DataCt = fileReader



                SetCursorPos(NewPos.getPosX(305), NewPos.getPosY(356)) '305,356按合計欄位頁籤
                setMouseClick("left", 2)
                Thread.Sleep(2 * 1000)

                SetCursorPos(NewPos.getPosX(305), NewPos.getPosY(248)) '305,248回第一筆
                setMouseClick("left", 2)
                Thread.Sleep(2 * 1000)

                SetCursorPos(NewPos.getPosX(544), NewPos.getPosY(250)) '544, 250 按轉出excel
                setMouseClick("left", 2)

                SetCursorPos(NewPos.getPosX(516), NewPos.getPosY(730)) '516,730 按確定
                setMouseClick("left", 2)
                Thread.Sleep(2 * 1000)
                setSendKeys("{RIGHT}", 1) '按右,不開excel
                setSendEnter(0)
                debug += 1
                cmd_test.cmd("cd C:\Users\udev77\Documents\COSMOS_ERP\C_Data")
                debug += 1
                '複製並改名到新路徑
                'MsgBox("move POSI49_2.XLSX " & mydocpath & "\POSI49_2_" & NowDate & "_" & EndDate & "_" & "1" & ".XLSX")
                cmd_test.cmd("move POSI49_2.XLSX " & mydocpath & "\POSI49_2_" & StartDate & "_" & EndDate & "_" & "1" & ".XLSX")
                debug += 1



                For i As Integer = 2 To DataCt '第二筆以(POSTA.TA001 >= N'20200901') And (POSTA.TA001 <= N'20200910')後需要按下一頁


                    SetCursorPos(NewPos.getPosX(360), NewPos.getPosY(252)) '360, 252按下一筆
                    setMouseClick("left", 2)
                    Thread.Sleep(2 * 1000)
                    SetCursorPos(NewPos.getPosX(544), NewPos.getPosY(250)) '544, 250 按轉出excel
                    setMouseClick("left", 2)

                    SetCursorPos(NewPos.getPosX(516), NewPos.getPosY(730)) '516,730 按確定
                    setMouseClick("left", 2)
                    Thread.Sleep(2 * 1000)
                    setSendKeys("{RIGHT}", 1) '按右,不開excel
                    setSendEnter(0)
                    debug += 1
                    '複製並改名到新路徑
                    cmd_test.cmd("move POSI49_2.XLSX " & mydocpath & "\POSI49_2_" & StartDate & "_" & EndDate & "_" & i & ".XLSX")
                    debug += 1
                Next



                'not_EOL_str = Split(fileReader, vbCrLf)
                'str = Split(not_EOL_str(0), "=")
                'If String.Compare(str(0), "softpath") = 0 Then
                ' progPath = str(1)
                ' End If
                '     str = Split(not_EOL_str(1), "=")
                '     If String.Compare(str(0), "datapath") = 0 Then
                '     dataPath = str(1)
                '     dataPath2 = str(1)
                '     dataPath = str(1)
                ' End If
            Else
                MsgBox("檔案不存在")
            End If
        Else
            Dim del_file_path As String = docpath & Convert.ToString("\DataCt.txt")
            cmd_test.cmd("del " & del_file_path)
        End If












        'C:\Users\udev77\Documents\COSMOS_ERP\C_DATA\POSI49_1.XLSX
        'C:\Users\udev77\Documents\POSI49_1.XLSX

        'Dim save_path As String = "C:\Users\udev77\Documents\POSI49_" & NowDate & ".XLSX"
        'Thread.Sleep(10 * 1000)
        'SetCursorPos(653, 376) '653,376 按
        'setMouseClick("left", 2)
        'SendKeys.SendWait(save_path)
        'Thread.Sleep(10 * 1000)

        'SetCursorPos(516, 730) '516,730 按確定
        'setMouseClick("left", 2)
        'Thread.Sleep(10 * 1000)
        'setSendKeys("{RIGHT}", 1) '按右,不開excel
        'setSendEnter(0)
        SendKeys.SendWait("%(X)")
        SendKeys.SendWait("{X}")
        'setPerfReport(NowDate, NowDate, hwd1, 60) '當日業績報表
        'SetCursorPos(218, 178)
        'setMouseClick("left", 2)
        'SendKeys.SendWait("COPR38{enter}") '輸入代號
        'setPerfReport(EarMonDate, NowDate, hwd1, 120) '累計業績報表
        SetCursorPos(835, 83) '到關閉系統位置
        Thread.Sleep(3 * 1000)
        setMouseClick("left", 2) '關閉系統
        Thread.Sleep(3 * 1000)

        'Dim str As Array
        'Dim not_EOL_str As Array


        'Dim dataPath As String = ""
        'Dim dataPath2 As String
        'Dim progPath As String
        '    Dim dirs As Array
        '    Dim dir As String

        '    Dim thisDate1 As Date = DateTime.Now
        '    Dim root As String = dataPath
        '    Dim file_count As Integer = 0
        '    Dim file_name1 As String = ""
        '    Dim file_dir1 As String = ""
        '    Dim file_name2 As String = ""
        '    Dim file_dir2 As String = ""
        '    Dim lines As String
        '    dirs = Directory.GetFiles(root, "COPR38" & thisDate1.ToString("yyyyMMdd") & "*.xlsx")
        '    For Each dir In dirs
        '        If (File.Exists(dir)) Then
        '            file_count += 1
        '            If file_count = 1 Then
        '                file_dir1 = dir
        '                file_name1 = search_file_name
        '                file_name1 = Path.GetFileName(dir)
        '                MsgBox("file_name1:" & file_name1)
        '                Dim temp_data1 As String = file_name1
        '                儲存內容
        '                lines = temp_data1
        '                Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\temp.txt"), False, System.Text.Encoding.GetEncoding(950))
        '                    MsgBox(lines)
        '                    For Each line As String In lines
        '                        outputFile.Write(line)
        '                    Next
        '                End Using
        '            End If
        '            If file_name1 <> "" And file_count = 2 Then
        '                file_dir2 = dir
        '                file_name2 = search_file_name
        '                file_name2 = Path.GetFileName(dir)
        '                MsgBox("file_name2:" & file_name2)
        '                Dim temp_data1 As String = file_name1
        '                Dim temp_data2 As String = file_name2
        '                儲存內容
        '                lines = temp_data1
        '                lines += vbCrLf
        '                lines += temp_data2
        '                Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\temp.txt"), False, System.Text.Encoding.GetEncoding(950))
        '                    MsgBox(lines)
        '                    For Each line As String In lines
        '                        outputFile.Write(line)
        '                    Next
        '                End Using

        '                If ProgressBarFrom.getBarValue = 100 Then
        '                    ProgressBarFrom.closeBar()
        '                End If
        '                P rogressBarFrom.addBarValue(100000)

        '            End If
        '            If file_count = 2 Then
        '                Exit For
        '            End If
        '        Else
        '            MsgBox("請檢查路徑")
        '        End If
        '    Next
        '    Me.Close()


        Me.Close()

    End Sub



    Private Sub Form1_Activated(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Activated
        Me.Hide()
        Me.Visible = False
    End Sub
    Public Sub setPerfReport(EarMonDate As String, NowDate As String, hwd1 As IntPtr, WaitingSec As Integer)
        setSendTab(3, 1)
        SendKeys.Send("^A")
        setSendEnter(3)
        Thread.Sleep(10 * 1000)
        'SetCursorPos(302, 451) '302,451位置
        'setMouseClick("left", 2)
        'setSendTab(1, 2)
        'SetCursorPos(330, 552) '330,552位置
        'setMouseClick("left", 2)

        inputDate(EarMonDate) '輸入開始日期
        setSendTab(1, 2)
        Thread.Sleep(10 * 1000)
        'SetCursorPos(330, 590) '330,590位置
        'setMouseClick("left", 2)
        inputDate(NowDate) '輸入結束日期
        'setSendTab(11, 1)
        SetCursorPos(997, 266) '997,266位置
        setMouseClick("left", 2)
        setSendEnter(1)
        'setSendEnter(2)
        SetCursorPos(645, 550) '645, 550 按確定
        setMouseClick("left", 0)
        setSendEnter(1)
        SetCursorPos(258, 93) '258,93 按報表工作佇列
        setMouseClick("left", 2)
        Dim hwd As IntPtr = FindWindow(vbNullString, "佇列工作控制台")
        SetForegroundWindow(hwd)
        SetCursorPos(500, 431) '500, 431 按報表
        setMouseClick("left", WaitingSec)
        setSendEnter(2)
        SetCursorPos(480, 369) '480,369 存成excel
        setMouseClick("left", 0)
        setSendEnter(1) '按enter
        setSendKeys("{RIGHT}", 1) '按右,不開excel
        setSendEnter(0) '
        SetCursorPos(964, 343) '964, 343 關閉報表預覽
        setMouseClick("left", 1)
        SetCursorPos(947, 313) '947, 313 關閉報表工作佇列
        setMouseClick("left", 0)
    End Sub

    Public Sub inputDate(newDate As String)
        Dim date_ary() As String
        date_ary = Split(newDate, "/")
        SendKeys.SendWait(date_ary(0)) '輸入開始日期
        Thread.Sleep(1000)
        SendKeys.SendWait(date_ary(1))
        Thread.Sleep(1000)
        SendKeys.SendWait(date_ary(2))
        Thread.Sleep(2000)
    End Sub

    Public Sub setMouseClick(str As String, sleepSec As Integer)
        If String.Equals(str, "left") Then
            mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        ElseIf String.Equals(str, "middle") Then
            mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
            mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
        ElseIf String.Equals(str, "right") Then
            mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        End If
        Thread.Sleep(sleepSec * 1000)
    End Sub

    Public Overloads Sub setSendEnter(sleepSec As Integer)
        SendKeys.SendWait("{enter}")
        Thread.Sleep(sleepSec * 1000)
    End Sub

    Public Overloads Sub setSendTab(tab_times As Integer, sleepSec As Integer)
        Dim i As Integer = 0
        Do
            SendKeys.SendWait("{tab}")
            Thread.Sleep(sleepSec * 1000)
            i += 1
        Loop Until i = tab_times
    End Sub

    Public Overloads Sub setSendKeys(sendKey As String, sleepSec As Integer)
        SendKeys.SendWait(sendKey)
        Thread.Sleep(sleepSec * 1000)
    End Sub

    Public Overloads Sub setSendKeys(sendKey As String)
        SendKeys.SendWait(sendKey)
        Thread.Sleep(2 * 1000)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs)
        Me.Close()
    End Sub

    Private Sub kbHook_KeyDown(ByVal Key As System.Windows.Forms.Keys) Handles kbHook.KeyDown
        'MsgBox(Key)
        If Key = 192 Then '112 F1 68 D
            Me.Close()
        End If
    End Sub

    Private Sub kbHook_KeyUp(ByVal Key As System.Windows.Forms.Keys) Handles kbHook.KeyUp
        'MsgBox(Key)
    End Sub


End Class

Public Class KeyboardHook

    <DllImport("User32.dll", CharSet:=CharSet.Auto, CallingConvention:=CallingConvention.StdCall)>
    Private Overloads Shared Function SetWindowsHookEx(ByVal idHook As Integer, ByVal HookProc As KBDLLHookProc, ByVal hInstance As IntPtr, ByVal wParam As Integer) As Integer
    End Function
    <DllImport("User32.dll", CharSet:=CharSet.Auto, CallingConvention:=CallingConvention.StdCall)>
    Private Overloads Shared Function CallNextHookEx(ByVal idHook As Integer, ByVal nCode As Integer, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Integer
    End Function
    <DllImport("User32.dll", CharSet:=CharSet.Auto, CallingConvention:=CallingConvention.StdCall)>
    Private Overloads Shared Function UnhookWindowsHookEx(ByVal idHook As Integer) As Boolean
    End Function

    <StructLayout(LayoutKind.Sequential)>
    Private Structure KBDLLHOOKSTRUCT
        Public vkCode As UInt32
        Public scanCode As UInt32
        Public flags As KBDLLHOOKSTRUCTFlags
        Public time As UInt32
        Public dwExtraInfo As UIntPtr
    End Structure

    <Flags()>
    Private Enum KBDLLHOOKSTRUCTFlags As UInt32
        LLKHF_EXTENDED = &H1
        LLKHF_INJECTED = &H10
        LLKHF_ALTDOWN = &H20
        LLKHF_UP = &H80
    End Enum

    Public Shared Event KeyDown(ByVal Key As Keys)
    Public Shared Event KeyUp(ByVal Key As Keys)

    Private Const WH_KEYBOARD_LL As Integer = 13
    Private Const HC_ACTION As Integer = 0
    Private Const WM_KEYDOWN = &H100
    Private Const WM_KEYUP = &H101
    Private Const WM_SYSKEYDOWN = &H104
    Private Const WM_SYSKEYUP = &H105

    Private Delegate Function KBDLLHookProc(ByVal nCode As Integer, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Integer

    Private KBDLLHookProcDelegate As KBDLLHookProc = New KBDLLHookProc(AddressOf KeyboardProc)
    Private HHookID As IntPtr = IntPtr.Zero

    Private Function KeyboardProc(ByVal nCode As Integer, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Integer
        If (nCode = HC_ACTION) Then
            Dim struct As KBDLLHOOKSTRUCT
            Select Case wParam
                Case WM_KEYDOWN, WM_SYSKEYDOWN
                    RaiseEvent KeyDown(CType(CType(Marshal.PtrToStructure(lParam, struct.GetType()), KBDLLHOOKSTRUCT).vkCode, Keys))
                Case WM_KEYUP, WM_SYSKEYUP
                    RaiseEvent KeyUp(CType(CType(Marshal.PtrToStructure(lParam, struct.GetType()), KBDLLHOOKSTRUCT).vkCode, Keys))
            End Select
        End If
        Return CallNextHookEx(IntPtr.Zero, nCode, wParam, lParam)
    End Function

    Public Sub New()
        HHookID = SetWindowsHookEx(WH_KEYBOARD_LL, KBDLLHookProcDelegate, System.Runtime.InteropServices.Marshal.GetHINSTANCE(System.Reflection.Assembly.GetExecutingAssembly.GetModules()(0)).ToInt32, 0)
        If HHookID = IntPtr.Zero Then
            Throw New Exception("Could not set keyboard hook")
        End If
    End Sub

    Protected Overrides Sub Finalize()
        If Not HHookID = IntPtr.Zero Then
            UnhookWindowsHookEx(HHookID)
        End If
        MyBase.Finalize()
    End Sub

End Class

Public Class Cmd
    Public setpath As String '保存執行路徑的屬性
    Sub cmd(cmd_str As String)
        Dim str_arr() As String
        Dim shell_result As String
        str_arr = Split(cmd_str, " ")
        If String.Compare("cd", str_arr(0)) = 0 Then '是cd指令
            Dim i As Integer
            Dim last_cmd_str As String = ""
            For i = 1 To str_arr.Length - 1 '把cd後面的字串組起來
                last_cmd_str = last_cmd_str & " " & str_arr(i)
            Next
            setpath = last_cmd_str '並儲存
        Else '不是cd指令
            shell_result = shell("cmd.exe", "/k cd " & setpath & " & " & cmd_str)
        End If
    End Sub

    Public Function shell(ByVal command As String, ByVal argument As String) As Integer
        Dim oProcess As New Process()
        Dim oStartInfo As New ProcessStartInfo(command, argument)
        oStartInfo.WindowStyle = ProcessWindowStyle.Hidden
        oStartInfo.CreateNoWindow = True ''不顯示視窗
        oStartInfo.UseShellExecute = False
        oStartInfo.RedirectStandardOutput = True
        oProcess.StartInfo = oStartInfo
        oProcess.Start()
        waitForEnd(oProcess) 'wait
        Return 0
    End Function

    Public Sub waitForEnd(oProcess As Process) 'NOP
        Dim sOutput As String
        Using oStreamReader As System.IO.StreamReader = oProcess.StandardOutput
            sOutput = oStreamReader.ReadToEnd()
        End Using
    End Sub

End Class

Public Class ScrnPt

    Dim OrigSpecX As Integer = 0
    Dim OrigCtrX As Integer = 0
    Dim OrigSpecY As Integer = 0
    Dim OrigCtrY As Integer = 0
    Dim NewCtrX As Integer = 0
    Dim NewCtrY As Integer = 0
    Public NewSpecX As Integer = 0
    Public NewSpecY As Integer = 0

    Public Sub New(OrigSizeX As Integer, OrigSizeY As Integer, NewSizeX As Integer, NewSizeY As Integer)
        '原螢幕中心點
        Me.OrigCtrX = OrigSizeX / 2
        Me.OrigCtrY = OrigSizeY / 2
        '新螢幕中心點
        Me.NewCtrX = NewSizeX / 2
        Me.NewCtrY = NewSizeY / 2
    End Sub

    Public Function getPosX(OrigSpecX As Integer)
        Me.NewSpecX = Me.NewCtrX - (Me.OrigCtrX - OrigSpecX)
        Return Me.NewSpecX
    End Function

    Public Function getPosY(OrigSpecY As Integer)
        Me.NewSpecY = Me.NewCtrY - (Me.OrigCtrY - OrigSpecY)
        Return Me.NewSpecY
    End Function

End Class

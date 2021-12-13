Public Class Form1
    Private Declare Function OpenProcess Lib "kernel32" (ByVal dwDesiredAccess As Integer, ByVal bInheritHandle As Integer, ByVal dwProcessId As Integer) As Integer
    'Private Declare Function WaitForSingleObject Lib "kernel32" (ByVal hHandle As Long, ByVal dwMilliseconds As Long) As Long
    Private Declare Function CloseHandle Lib "kernel32" (ByVal hObject As Integer) As Integer
    Private Declare Function GetExitCodeProcess Lib "kernel32" (ByVal hProcess As String, lpExitCode As String) As String
    'Private Declare Function TerminateProcess Lib "kernel32" (ByVal hProcess As Long, ByVal uExitCode As Long) As Long
    'Private Declare Function GetForegroundWindow Lib "user32" () As Long
    'Private Declare Function IsWindow Lib "user32" (ByVal hwnd As Long) As Long

    Const PROCESS_QUERY_INFORMATION = &H400
    Const STILL_ALIVE = &H103
    'Const INFIN99vE = &HFFFF

    Private ExitCode As Integer
    Private hProcess As Integer
    'Private isDone As Long

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        'Dim str_arr() As String
        'Dim cmd_str As String = "123456"
        'str_arr = Split(cmd_str, vbNewLine)
        'MsgBox(str_arr(0))
        'Dim cmd_test As Cmd = New Cmd()
        'cmd_test.cmd("cd /d S:\網通部\◎資訊\test\")
        'cmd_test.cmd("git add .")
        'cmd_test.cmd("git commit -m " & Chr(34) & "New file" & Chr(34))
        'cmd_test.cmd("git push")

        'test()

        'start /w cmd.exe /c start /w & cd /d S:\網通部\◎資訊\test\
        'start /w cmd.exe /c & cd /d S:\網通部\◎資訊\test\ & git add .
        'start /w cmd.exe /c & cd /d S:\網通部\◎資訊\test\ & git commit -m "New file"
        'start /w cmd.exe /c & cd /d S:\網通部\◎資訊\test\ & git push
        'MsgBox(0)
        'MsgBox("start /w cmd.exe /c " & Chr(38) & " cd /d S:\網通部\◎資訊\test\")
        'Shell("cmd.exe /c cd /d S:\網通部\◎資訊\test\", vbHide)

        'Threading.Thread.Sleep(5000)
        'Shell("cmd.exe /c cd /d S:\網通部\◎資訊\test\ & git add .", vbHide)
        'Threading.Thread.Sleep(5000)
        'Shell("cmd.exe /c cd /d S:\網通部\◎資訊\test\ & git commit -m " & Chr(34) & "New file" & Chr(34), vbHide)
        'Threading.Thread.Sleep(5000)
        'Shell("cmd.exe /c cd /d S:\網通部\◎資訊\test\ & git push", vbHide)
        'Threading.Thread.Sleep(5000)

        'Dim pid As Long
        'Dim ExitEvent As Long
        'pid = Shell("cmd.exe", vbNormalFocus)
        'hProcess = OpenProcess(PROCESS_QUERY_INFORMATION + SYNCHRONIZE, 0, pid)
        'ExitEvent = WaitForSingleObject(hProcess, INFINITE)
        'Call CloseHandle(hProcess)



        'cmd.exe /c 不顯示 vbHide
        'cmd.exe /k 顯示 vbNormalNoFocus
    End Sub


    Public Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click

        Label1.Text = shellt()
        'Label1.Text = shelltest("cmd.exe", "start echo 123 & echo done")
        'Dim pid As Long
        'pid = Shell("C:\Users\udev77\Desktop\a.bat", vbNormalFocus)

        'hProcess = OpenProcess(PROCESS_QUERY_INFORMATION, 0, pid)
        'Do
        '    Call GetExitCodeProcess(hProcess, ExitCode)
        '    'DoEvents()
        'Loop While ExitCode = STILL_ALIVE
        'Call CloseHandle(hProcess)
        'MsgBox("运行结束")
    End Sub

    Public Sub test()

    End Sub
    Public Function shellt()
        'Return shelltest("cmd.exe", "/k cd /d S:\網通部\◎資訊\test\ & git add . & echo done")
        Return 0
    End Function
    Public Function shelltest(ByVal command As String, ByVal argument As String) As String
        Dim oProcess As New Process()
        'Dim oStartInfo As New ProcessStartInfo("C:\Users\udev77\Desktop\a.bat", "")
        'Dim oStartInfo As New ProcessStartInfo("cmd.exe", "start echo 123")
        Dim oStartInfo As New ProcessStartInfo(command, argument)
        'Dim oStartInfo As New ProcessStartInfo("cmd.exe", "/k cd /d S:\網通部\◎資訊\test\ & git add . & @echo done")
        oStartInfo.UseShellExecute = False
        oStartInfo.RedirectStandardOutput = True
        oProcess.StartInfo = oStartInfo
        oProcess.Start()

        Dim sOutput As String
        Using oStreamReader As System.IO.StreamReader = oProcess.StandardOutput
            sOutput = oStreamReader.ReadToEnd()
            MsgBox(sOutput)
        End Using

        Dim str_arr() As String
        Dim cmd_str As String = sOutput
        str_arr = Split(cmd_str, vbNewLine)
        'MsgBox(str_arr.Length)
        'MsgBox(str_arr(0))
        Return str_arr(0)
    End Function

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim cmd_test As Cmd = New Cmd()
        'cmd_test.cmd("cd /d S:\網通部\◎資訊\test\")
        'cmd_test.cmd("git add .")
        'cmd_test.cmd("git commit -m " & Chr(34) & "New file" & Chr(34))
        'cmd_test.cmd("git push")
        cmd_test.cmd("cd C:\Users\udev77\Documents\COSMOS_ERP\C_Data")
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim NowDate As String
        NowDate = "20200801" '測試用日期
        '複製並改名到新路徑
        MsgBox(mydocpath)
        'MsgBox("move POSI49_2.XLSX C:\" & mydocpath & "\POSI49_2_" & NowDate & "_" & "1" & ".XLSX")
        'cmd_test.cmd("move POSI49_2.XLSX " & mydocpath & "\POSI49_2_" & NowDate & "_" & "1" & ".XLSX")
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
        oStartInfo.UseShellExecute = False
        oStartInfo.RedirectStandardOutput = True
        oProcess.StartInfo = oStartInfo
        oProcess.Start()
        NOP(oProcess) 'wait
        Return 0
    End Function

    Public Sub NOP(oProcess As Process)
        Dim sOutput As String
        Using oStreamReader As System.IO.StreamReader = oProcess.StandardOutput
            sOutput = oStreamReader.ReadToEnd()
        End Using
    End Sub

End Class

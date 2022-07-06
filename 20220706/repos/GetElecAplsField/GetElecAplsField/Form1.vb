﻿Imports System.IO
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
        'Me.Show()
        Dim hwd As IntPtr
        Dim hwd1 As IntPtr
        'Label1.Text = "產生報表中，勿移動滑鼠及操控鍵盤"
        'Label2.Text = "F1關閉"
        'Label1.Refresh()
        'Label2.Refresh()
        Me.Hide()
        Me.Visible = False

        Dim NowDate As String = System.DateTime.Now
        Dim EarMonDate As String = DateTime.Parse(NowDate).ToString("yyy/MM/") & "01"
        NowDate = DateTime.Parse(NowDate).ToString("yyy/MM/dd")
        a.StartInfo.FileName = "C:\Conductor\C_dsbin\MainMenu.exe"
        a.Start()
        hwd = FindWindow(vbNullString, "鼎新電腦 Cosmos ERP")
        If hwd.Equals(IntPtr.Zero) Then '若已開啟就不等待秒數
            Thread.Sleep(13000)
        Else
            Thread.Sleep(3000)
        End If
        SetCursorPos(790, 497) '輸入密碼座標
        setMouseClick("left", 2)
        setSendKeys("01439{enter}", 10)

        SetCursorPos(258, 93) '258,93 按報表工作佇列
        setMouseClick("left", 2)
        hwd1 = FindWindow(vbNullString, "佇列工作控制台")
        SetForegroundWindow(hwd1)
        SetCursorPos(691, 390) '691, 390 週期性
        setMouseClick("left", 2)
        'SetCursorPos(500, 431) '500, 431 按報表1

        SetCursorPos(578, 443) '578, 443 右欄第二列
        setMouseClick("left", 2)
        setSendEnter(2)
        SetCursorPos(480, 369) '480,369 存成excel
        setMouseClick("left", 0)
        setSendEnter(1) '按enter
        setSendKeys("{RIGHT}", 1) '按右,不開excel
        setSendEnter(0) '

        SetCursorPos(964, 343) '964, 343 關閉報表預覽
        setMouseClick("left", 1)



        'SetCursorPos(460, 443) '460,443 左欄第二列
        'setMouseClick("left", 2)
        ''578,443
        ''SetCursorPos(500, 446) '500, 446 按報表2
        'SetCursorPos(578, 443) '578, 443 右欄第二列
        'setMouseClick("left", 2)
        'setSendEnter(2)
        'SetCursorPos(480, 369) '480,369 存成excel
        'setMouseClick("left", 0)
        'setSendEnter(1) '按enter
        'setSendKeys("{RIGHT}", 1) '按右,不開excel
        'setSendEnter(0) '

        'SetCursorPos(947, 313) '947, 313 關閉報表工作佇列
        'setMouseClick("left", 0)



        SetCursorPos(835, 83) '到關閉系統位置
        setMouseClick("left", 2) '關閉系統

        Dim str As Array
        Dim not_EOL_str As Array
        Dim fileReader As String
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim dataPath As String = ""
        Dim dataPath2 As String
        Dim progPath As String
        Dim dirs As Array
        Dim dir As String
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\pathfile.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\pathfile.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(0), "=")
            If String.Compare(str(0), "softpath") = 0 Then
                progPath = str(1)
            End If
            str = Split(not_EOL_str(1), "=")
            If String.Compare(str(0), "datapath") = 0 Then
                dataPath = str(1)
                dataPath2 = str(1)
                dataPath = str(1)
            End If
        Else
            'MsgBox("檔案不存在")
        End If
        Dim thisDate1 As Date = DateTime.Now
        Dim root As String = dataPath
        Dim file_count As Integer = 0
        Dim file_name1 As String = ""
        Dim file_dir1 As String = ""
        Dim file_name2 As String = ""
        Dim file_dir2 As String = ""
        Dim lines As String
        dirs = Directory.GetFiles(root, "COPR38" & thisDate1.ToString("yyyyMMdd") & "*.xlsx")
        For Each dir In dirs
            If (File.Exists(dir)) Then
                file_count += 1
                If file_count = 1 Then
                    file_dir1 = dir
                    'file_name1 = search_file_name
                    file_name1 = Path.GetFileName(dir)
                    'MsgBox("file_name1:" & file_name1)
                    Dim temp_data1 As String = file_name1
                    '儲存內容
                    lines = temp_data1
                    Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\temp.txt"), False, System.Text.Encoding.GetEncoding(950))
                        'MsgBox(lines)
                        For Each line As String In lines
                            outputFile.Write(line)
                        Next
                    End Using
                End If
                If file_name1 <> "" And file_count = 2 Then
                    file_dir2 = dir
                    'file_name2 = search_file_name
                    file_name2 = Path.GetFileName(dir)
                    'MsgBox("file_name2:" & file_name2)
                    Dim temp_data1 As String = file_name1
                    Dim temp_data2 As String = file_name2
                    '儲存內容
                    lines = temp_data1
                    lines += vbCrLf
                    lines += temp_data2
                    Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\temp.txt"), False, System.Text.Encoding.GetEncoding(950))
                        'MsgBox(lines)
                        For Each line As String In lines
                            outputFile.Write(line)
                        Next
                    End Using

                    'If ProgressBarFrom.getBarValue = 100 Then
                    'ProgressBarFrom.closeBar()
                    'End If
                    'P rogressBarFrom.addBarValue(100000)

                End If
                If file_count = 2 Then
                    Exit For
                End If
            Else
                MsgBox("請檢查路徑")
            End If
        Next
        'Me.Close()

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
        hwd1 = FindWindow(vbNullString, "佇列工作控制台")
        SetForegroundWindow(hwd1)
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

    'Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    'End Sub
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

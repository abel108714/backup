Imports System.IO
Imports System.Threading
Imports System.Runtime.InteropServices
Imports IWshRuntimeLibrary

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
    Private Declare Function GetForegroundWindow Lib "user32" () As IntPtr


    Public Const MOUSEEVENTF_LEFTDOWN = &H2
    Public Const MOUSEEVENTF_LEFTUP = &H4
    Public Const MOUSEEVENTF_MIDDLEDOWN = &H20
    Public Const MOUSEEVENTF_MIDDLEUP = &H40
    Public Const MOUSEEVENTF_RIGHTDOWN = &H8
    Public Const MOUSEEVENTF_RIGHTUP = &H10
    Public Const MOUSEEVENTF_MOVE = &H1
    Dim a As New Process

    Private Declare Function GetDC Lib "user32" (ByVal hwnd As Int32) As Int32
    Private Declare Function ReleaseDC Lib "user32" (ByVal hwnd As Int32, ByVal hdc As Int32) As Int32
    Private Declare Function GetPixel Lib "gdi32" (ByVal hdc As Int32, ByVal x As Int32, ByVal y As Int32) As Int32

    Public Function Good_GetPixel(ByVal x As Int16, ByVal y As Int16) As Color
        Dim kk As Int32 = GetPixel(GetDC(0), x, y)
        Dim Color As Color = ColorTranslator.FromWin32(kk)
        ReleaseDC(0, GetDC(0))
        Return Color
    End Function

    Private Function get_Color(ByVal x As Int16, ByVal y As Int16) As String
        Dim c As Color = Good_GetPixel(x, y)   'Return a color
        Dim rgbstr = c.R & "." & c.G & "." & c.B
        'MsgBox("RGB = " & c.R & "." & c.G & "." & c.B)
        'Label1.BackColor = c    '某個標籤的背景顏色變換指定顏色
        Return rgbstr
    End Function
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'Me.Show()
        Dim hwd As IntPtr
        Dim hwd1 As IntPtr
        Dim nowhwd As IntPtr
        'Label1.Text = "產生報表中，勿移動滑鼠及操控鍵盤"
        'Label2.Text = "F1關閉"
        'Label1.Refresh()
        'Label2.Refresh()
        Me.Hide()
        Me.Visible = False

        Dim NowDate As String = System.DateTime.Now
        'MsgBox(NowDate)
        Dim EarMonDate As String = DateTime.Parse(NowDate).ToString("yyy/MM/") & "01"
        NowDate = DateTime.Parse(NowDate).ToString("yyy/MM/dd")
        Dim screenWidth As Integer = Screen.PrimaryScreen.Bounds.Width
        Dim screenHeight As Integer = Screen.PrimaryScreen.Bounds.Height
        'Dim NewPt As ScrnPt = New ScrnPt(1280, 1024, 1366, 768)
        Dim NewPt As ScrnPt = New ScrnPt(1280, 1024, 1366, 768)
        Dim NewPt2 As ScrnPt = New ScrnPt(1366, 768, screenWidth, screenHeight)
        'MsgBox(get_Color(NewPt.getPosX(790), NewPt.getPosY(497)))
        a.StartInfo.FileName = "C:\Conductor\C_dsbin\MainMenu.exe"
        a.Start()
        hwd = FindWindow(vbNullString, "鼎新電腦 Cosmos ERP")

        '取得目前系統中前景程式的視窗(Handle)
        nowhwd = GetForegroundWindow()
        If hwd <> nowhwd Then
            SetForegroundWindow(hwd)
        End If

        'If hwd.Equals(IntPtr.Zero) Then '若已開啟就不等待秒數
        'Thread.Sleep(13000)
        'Else
        ' Thread.Sleep(3000)
        ' End If

        While get_Color(NewPt2.getPosX(NewPt.getPosX(790)), NewPt2.getPosY(NewPt.getPosY(497))) <> "255.255.255"
            Thread.Sleep(1000)
            If hwd.Equals(IntPtr.Zero) = False And get_Color(NewPt2.getPosX(NewPt.getPosX(790)), NewPt2.getPosY(NewPt.getPosY(497))) = "255.255.255" Then
                Thread.Sleep(1000)
                Exit While
            End If
        End While
        'Dictionary<string, string> openWith = new Dictionary<string, string>();
        Dim openWith As Dictionary(Of String, Integer) =
            New Dictionary(Of String, Integer)

        Dim sArray() As String = {
            "歷史交易記錄表(全部)[下午4:00]",
            "歷史交易記錄表(機具)[下午4:00]",
            "業務員別銷貨期報表(今日)[下午4:00]",
            "業務員別銷貨期報表(本月累計)[下午4:00]",
            "歷史交易記錄表(全部)[下午5:00]",
            "歷史交易記錄表(機具)[下午5:40]",
            "業務員別銷貨期報表(今日)[下午5:40]",
            "業務員別銷貨期報表(本月累計)[下午5:40]"
        }

        For Each element In sArray
            openWith(element) = i;
                 i = i + 1
        Next element

        Dim sArray() As String = {
            "歷史交易記錄表(全部)[下午4:00]",
            "歷史交易記錄表(機具)[下午4:00]",
            "業務員別銷貨期報表(今日)[下午4:00]",
            "業務員別銷貨期報表(本月累計)[下午4:00]",
            "歷史交易記錄表(全部)[下午5:00]",
            "歷史交易記錄表(機具)[下午5:40]",
            "業務員別銷貨期報表(今日)[下午5:40]",
            "業務員別銷貨期報表(本月累計)[下午5:40]"
        }

        For Each element In sArray
            openWith(element) = i;
                 i = i + 1
        Next element
        'get_Color(NewPt.getPosX(790), NewPt.getPosY(497))

        'Shell("C:\auto\GetPicText.py")
        'MsgBox(pyResult.ReadAll)
        'Dim pyr As String
        'pyShell = CreateObject("Wscript.Shell")
        'Color = icolor
        'Imagepath = ipath
        'pyColorVerify = "C:\auto\GetPicText.py"
        'pyOperation = pyShell.Exec(pyColorVerify)
        'pyResult = pyOperation.StdOut
        'wait(1)
        'MsgBox(pyResult.ReadAll)

        'Dim cmd_test As Cmd = New Cmd()
        'cmd_test.cmd("cd /d C:\auto\")
        'cmd_test.cmd("GetPicText.py")

        'Dim shell As WshShell = WScript.CreateObject("WScript.Shell")
        'MsgBox(shell.ExpandEnvironmentStrings("%windir%"))
        'Dim pyr As String
        'pyShell = CreateObject("Wscript.Shell")

        'Color = icolor
        'Imagepath = ipath
        'pyColorVerify = "python ""C:\Users\a272099\Desktop\Python\codes\Verifycolor.py""" & " " & Color & " " & ImagePath
        'pyOperation = pyShell.Exec(pyColorVerify)
        'pyResult = pyOperation.StdOut
        'wait(1)
        'MsgBox(pyResult.ReadAll)


        'pyr = pyResult.ReadAll

        'MsgBox(pyr)

        'MsgBox("1233")
        'Dim shell As WshShell = New WshShell
        Dim wshshell As Object
        'Dim wscript As Object
        'wshshell = wscript.CreateObject("WScript.Shell")
        wshshell = CreateObject("WScript.Shell")

        Dim pyr As String
        Dim pyColorVerify As String
        Dim pyOperation As Object
        'Dim pyResult As String
        Dim pyResult As Object
        'Dim shell As WshShell = New WScript.CreateObject("C:\Windows\System32\wscript.exe")

        'MsgBox(wshshell.ExpandEnvironmentStrings("%windir%"))
        pyColorVerify = "python C:\auto\GetPicText.py"
        'MsgBox(pyColorVerify)
        'Dim procID As Integer
        ' Run calculator.
        MsgBox("0")

        'pyOperation = wshshell.exec("C:\auto\GetPicText.exe")
        'MsgBox("1")
        'MsgBox(pyOperation)
        'pyResult = pyOperation.StdOut
        'MsgBox(pyResult.ReadAll)
        'MsgBox(procID)

        'MsgBox("2")
        'pyOperation = wshshell.exec(pyColorVerify)

        'wait(1)
        'MsgBox(pyResult.ReadAll)


        'pyr = pyResult.ReadAll

        'MsgBox(pyr)

        Thread.Sleep(1000)
        Testing()

        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(790)), NewPt2.getPosY(NewPt.getPosY(497))) '輸入密碼座標

        setMouseClick("left", 5)
        setSendKeys("01439{enter}", 10)

        SetCursorPos(258, 93) '258,93 按報表工作佇列
        setMouseClick("left", 6)
        hwd1 = FindWindow(vbNullString, "佇列工作控制台")
        'MsgBox(hwd1)
        '取得目前系統中前景程式的視窗(Handle)
        nowhwd = GetForegroundWindow()
        'MsgBox(nowhwd)
        'MsgBox(nowhwd)
        'MsgBox(hwd1)
        If hwd1 <> nowhwd Then
            SetForegroundWindow(hwd1)
            'MsgBox(nowhwd)
        End If

        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(691)), NewPt2.getPosY(NewPt.getPosY(390))) '691, 390 週期性
        setMouseClick("left", 6)
        'If Not (Format(Now, "hh:mm") >= "16:00") And (Format(Now, "hh:mm") <="16:59") Then
        'SetCursorPos(573, 392) '578, 443 右欄第二列
        'setMouseClick("left", 2)
        'End If
        'If (Format(Now, "hh:mm") >= "16:00") And (Format(Now, "hh:mm") <= "16:59") Then
        ' SetCursorPos(NewPt.getPosX(460), NewPt.getPosY(443 + 17)) '460,443 左欄第一列
        'Else
        ''SetCursorPos(573, 392)
        'setSendKeys("{DOWN}", 1)
        'End If
        ''SetCursorPos(500, 431) '500, 431 按報表1
        '---------------------------------------------------------------------------
        'SetCursorPos(NewPt.getPosX(460), NewPt.getPosY(443 - 17)) '460,443 左欄第一列
        'setMouseClick("left", 2)
        'SetCursorPos(NewPt.getPosX(578), NewPt.getPosY(443)) '578, 443 右欄第二列
        'setMouseClick("left", 2)
        'While get_Color(922, 556) <> "255.255.255"
        '    Thread.Sleep(1000)
        '    If get_Color(922, 556) = "255.255.255" Then
        '        Thread.Sleep(1000)
        '        Exit While
        '    End If
        'End While
        ''---------------------------------------------------------------------------
        'setSendEnter(2)01439

        'SetCursorPos(NewPt.getPosX(480), NewPt.getPosY(369)) '480,369 存成excel
        'setMouseClick("left", 0)
        'setSendEnter(1) '按enter
        'setSendKeys("{RIGHT}", 1) '按右,不開excel伴　
        'setSendEnter(0) '

        'SetCursorPos(NewPt.getPosX(964), NewPt.getPosY(343)) '964, 343 關閉報表預覽
        'setMouseClick("left", 1)

        '---------------------------------------------------------------------------
        If (Format(Now, "HH:mm") >= "16:00") And (Format(Now, "HH:mm") <= "16:59") Then
            'SetCursorPos(NewPt.getPosX(460), NewPt.getPosY(443)) '460,443 左欄第一列
            'setMouseClick("left", 2)
            'MsgBox("11")
        Else
            'MsgBox("11")
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            'MsgBox("12")
            setMouseClick("left", 2)
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            setMouseClick("left", 2)
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            setMouseClick("left", 2)
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            setMouseClick("left", 2)
            'MsgBox("13")
        End If
        'If (Format(Now, "HH:mm") >= "17:40") Then
        If (Format(Now, "HH:mm") >= "16:00") And (Format(Now, "HH:mm") <= "16:59") Then
        Else
            'setMouseClick("left", 2)
            SetCursorPos(NewPt2.getPosX(NewPt.getPosX(578)), NewPt2.getPosY(NewPt.getPosY(443))) '578, 443 右欄第二列
            setMouseClick("left", 2)
            '---------------------------------------------------------------------------
            setSendEnter(2)
            SetCursorPos(NewPt2.getPosX(NewPt.getPosX(480)), NewPt2.getPosY(NewPt.getPosY(369))) '480,369 存成excel
            setMouseClick("left", 2)
            setSendEnter(1) '按enter
            'MsgBox("1")
            setSendKeys("{RIGHT}", 2) '按右,不開excel　
            'MsgBox("1")
            setSendEnter(1) '
            setSendKeys("{RIGHT}", 2) '按右,不開excel　
            'MsgBox("1")
            setSendEnter(1) '
            'MsgBox("1")
            SetCursorPos(NewPt2.getPosX(NewPt.getPosX(964)), NewPt2.getPosY(NewPt.getPosY(343))) '964, 343 關閉報表預覽
            setMouseClick("left", 1)
            'MsgBox("13")
        End If
        'MsgBox("14")
        '---------------------------------------------------------------------------

        If (Format(Now, "HH:mm") >= "16:00") And (Format(Now, "HH:mm") <= "16:59") Then

            SetCursorPos(NewPt2.getPosX(NewPt.getPosX(460)), NewPt2.getPosY(NewPt.getPosY(443))) '460,443 左欄第二列  改第三
            setMouseClick("left", 2)

            'MsgBox("1")
        Else
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            setMouseClick("left", 2)
            'MsgBox("1")
            '多按一下跳過門市
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置

            setMouseClick("left", 2)
            'MsgBox("2")
        End If
        'MsgBox("3")
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(578)), NewPt2.getPosY(NewPt.getPosY(443))) '578, 443 右欄第二列
        setMouseClick("left", 2)
        '---------------------------------------------------------------------------
        setSendEnter(2)
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(480)), NewPt2.getPosY(NewPt.getPosY(369))) '480,369 存成excel
        setMouseClick("left", 2)
        setSendEnter(2) '按enter
        setSendKeys("{RIGHT}", 2) '按右,不開excel
        setSendEnter(2) '
        setSendKeys("{RIGHT}", 2) '按右,不開excel
        setSendEnter(2) '
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(964)), NewPt2.getPosY(NewPt.getPosY(343))) '964, 343 關閉報表預覽
        setMouseClick("left", 1)

        '---------------------------------------------------------------------------
        'SetCursorPos(460, 443) '460,443 左欄第二列01439

        If (Format(Now, "HH:mm") >= "16:00") And (Format(Now, "HH:mm") <= "16:59") Then
            SetCursorPos(NewPt2.getPosX(NewPt.getPosX(460)), NewPt2.getPosY(NewPt.getPosY(443 + 17))) '460,460 左欄第三列  改第四
            setMouseClick("left", 2)
        Else
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            setMouseClick("left", 2)

        End If

        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(578)), NewPt2.getPosY(NewPt.getPosY(443))) '578, 443 右欄第二列
        setMouseClick("left", 2)

        '---------------------------------------------------------------------------
        setSendEnter(2)
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(480)), NewPt2.getPosY(NewPt.getPosY(369))) '480,369 存成excel
        setMouseClick("left", 2)
        setSendEnter(2) '按enter

        setSendKeys("{RIGHT}", 2) '按右,不開excel
        setSendEnter(2) '
        setSendKeys("{RIGHT}", 2) '按右,不開excel
        setSendEnter(2) '
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(964)), NewPt2.getPosY(NewPt.getPosY(343))) '964, 343 關閉報表預覽
        setMouseClick("left", 1)
        If (Format(Now, "HH:mm") >= "16:00") And (Format(Now, "HH:mm") <= "16:59") Then
            SetCursorPos(NewPt2.getPosX(NewPt.getPosX(460)), NewPt2.getPosY(NewPt.getPosY(443 + 17 + 17))) '460,460 左欄第三列  改第四
            setMouseClick("left", 2)
        Else
            SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
            setMouseClick("left", 2)

        End If

        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(578)), NewPt2.getPosY(NewPt.getPosY(443))) '578, 443 右欄第二列
        setMouseClick("left", 2)
        '---------------------------------------------------------------------------
        setSendEnter(2)
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(480)), NewPt2.getPosY(NewPt.getPosY(369))) '480,369 存成excel
        setMouseClick("left", 2)
        setSendEnter(2) '按enter
        setSendKeys("{RIGHT}", 2) '按右,不開excel
        setSendEnter(2) '
        setSendKeys("{RIGHT}", 2) '按右,不開excel
        setSendEnter(2) '
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(964)), NewPt2.getPosY(NewPt.getPosY(343))) '964, 343 關閉報表預覽
        setMouseClick("left", 1)

        'If (Format(Now, "HH:mm") >= "16:00") And (Format(Now, "HH:mm") <= "16:59") Then
        ' SetCursorPos(NewPt2.getPosX(NewPt.getPosX(460)), NewPt2.getPosY(NewPt.getPosY(443 + 17 + 17 + 17))) '460,460 左欄第三列  改第四
        ' setMouseClick("left", 2)
        'Else
        'SetCursorPos(NewPt2.getPosX(572), NewPt2.getPosY(390)) '點下拉箭頭位置
        'setMouseClick("left", 2)
        '
        'End If
        '
        'SetCursorPos(NewPt2.getPosX(NewPt.getPosX(578)), NewPt2.getPosY(NewPt.getPosY(443))) '578, 443 右欄第二列
        'setMouseClick("left", 2)
        '---------------------------------------------------------------------------
        'setSendEnter(2)
        'SetCursorPos(NewPt2.getPosX(NewPt.getPosX(480)), NewPt2.getPosY(NewPt.getPosY(369))) '480,369 存成excel
        'setMouseClick("left", 2)
        'setSendEnter(2) '按enter
        'setSendKeys("{RIGHT}", 2) '按右,不開excel
        'setSendEnter(2) '
        'setSendKeys("{RIGHT}", 2) '按右,不開excel
        'setSendEnter(2) '


        'SetCursorPos(NewPt2.getPosX(NewPt.getPosX(964)), NewPt2.getPosY(NewPt.getPosY(343))) '964, 343 關閉報表預覽
        'setMouseClick("left", 1)
        SetCursorPos(NewPt2.getPosX(NewPt.getPosX(947)), NewPt2.getPosY(NewPt.getPosY(313))) '947, 313 關閉報表工作佇列
        setMouseClick("left", 0)

        'setSendKeys("01439{enter}", 10)01439
        'SetCursorPos(100, 175) '到輸入代號位置100,175'setSendTab(3, 1) '到輸入代號位置
        'setMouseClick("left", 2)
        'SendKeys.SendWait("COPR38{enter}") '輸入代號
        'setPerfReport(NowDate, NowDate, hwd1, 60) '當日業績報表
        'SetCursorPos(218, 178)
        'setMouseClick("left", 2)
        'SendKeys.SendWait("COPR38{enter}") '輸入代號
        'setPerfReport(EarMonDate, NowDate, hwd1, 120) '累計業績報表
        SetCursorPos(835, 83) '到關閉系統位置
        setMouseClick("left", 2) '關閉系統

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

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub
    Public Function Testing() As String
        Dim strCmdLine As String
        Dim Test As String
        'strCmdLine = "-c -f -r" & " -hl:Razzamataz.elkdorf.com"
        strCmdLine = ""
        '("C:\auto\GetPicText.exe")
        Dim TestProcess As System.Diagnostics.Process
        Try
            TestProcess = New System.Diagnostics.Process
            TestProcess.StartInfo.FileName = "C:\auto\GetPicText.exe"
            TestProcess.StartInfo.Arguments = strCmdLine
            TestProcess.StartInfo.WindowStyle = Diagnostics.ProcessWindowStyle.Hidden

            TestProcess.StartInfo.CreateNoWindow = False ''不顯示視窗
            TestProcess.StartInfo.RedirectStandardOutput = True
            TestProcess.StartInfo.UseShellExecute = False
            TestProcess.Start()
            Dim strTestResults As String = TestProcess.StandardOutput.ReadToEnd()
            TestProcess.WaitForExit()
            Test = TestProcess.ExitCode.ToString & " - " & strTestResults
            MsgBox(Test)
            TestProcess.Close()
        Catch ex As Exception
            Test = "ERROR: No Results from Process" & " - " & ex.Message
            Return Test
        End Try
        Return Test
    End Function

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





﻿

Imports System.IO
Imports System.Threading
Imports System.Runtime.InteropServices
Imports Microsoft.Office.Interop.Excel
'Option Strict On
'Imports Excel = Microsoft.Office.Interop.Excel
'Imports Microsoft.Office

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

    Private Sub setInputData(str As String, sec As Integer)
        SetCursorPos(760, 184) '輸入客戶代號座標
        setMouseClick("left", sec)
        SetCursorPos(736, 245) '輸入客戶代號座標
        setMouseClick("left", sec)
        setSendKeys(str & "{enter}", sec)
        SetCursorPos(398, 295) '輸入客戶代號座標
        setMouseClick("left", sec)
        setSendKeys("{enter}", sec)
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'Me.Show()
        Dim hwd As IntPtr
        'Dim hwd1 As IntPtr
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
        Dim NewPt As ScrnPt = New ScrnPt(1280, 1024, 1366, 768)
        'MsgBox(get_Color(NewPt.getPosX(790), NewPt.getPosY(497)))
        'a.StartInfo.FileName = "C:\Conductor\C_dsbin\MainMenu.exe"
        'a.Start()
        'hwd = FindWindow(vbNullString, "鼎新電腦 Cosmos ERP")

        '取得目前系統中前景程式的視窗(Handle)
        'nowhwd = GetForegroundWindow()
        'If hwd <> nowhwd Then
        '    SetForegroundWindow(hwd)
        'End If

        'If hwd.Equals(IntPtr.Zero) Then '若已開啟就不等待秒數
        'Thread.Sleep(13000)
        'Else
        ' Thread.Sleep(3000)
        ' End If

        'While get_Color(NewPt.getPosX(790), NewPt.getPosY(497)) <> "255.255.255"
        'Thread.Sleep(1000)
        'If hwd.Equals(IntPtr.Zero) = False And get_Color(NewPt.getPosX(790), NewPt.getPosY(497)) = "255.255.255" Then
        'Thread.Sleep(1000)
        'Exit While
        'End If
        'End While

        Dim range As Object
        Dim xlApp_sou As Object
        Dim xlBook_sou As Object
        Dim xlsheet_sou As Object

        xlApp_sou = CreateObject("Excel.Application") '創建EXCEL應用類
        xlApp_sou.Visible = False 'True '設置EXCEL可見
        xlBook_sou = xlApp_sou.Workbooks.Open("C:\Users\udev77\Downloads" & "\★★營業單位組別_彙整五組(整理變更業績表TO立修).xlsx") '打開EXCEL工作簿


        Dim startRow As Integer
        Dim startSheet As Integer
        Dim i As Integer
        Dim j As Integer
        startRow = 2
        startSheet = 2
        i = startRow
        j = startSheet

        '聯盟  李永齊
        '實通團購    張嘉芬
        '流通連鎖    王瑲賢
        '電購  張玉玲
        '網路  吳佳螢





        'SetCursorPos(NewPt.getPosX(790), NewPt.getPosY(497)) '輸入密碼座標
        'setMouseClick("left", 2)
        'setSendKeys("01439{enter}", 10)

        'SetCursorPos(212, 174) '輸入報表代號座標
        'setMouseClick("left", 2)
        'setSendKeys("copr23{enter}", 10)


        'SetCursorPos(746, 274) '輸入客戶代號座標
        'SetCursorPos(760, 184) '輸入客戶代號座標
        'setMouseClick("left", 2)
        'SetCursorPos(736, 245) '輸入客戶代號座標
        'setMouseClick("left", 2)
        'Dim s As String
        's = "C069900004"
        'setSendKeys(s & "{enter}", 10)
        'SetCursorPos(398, 295) '輸入客戶代號座標
        'setMouseClick("left", 2)
        'setSendKeys("{enter}", 10)

        'setSendKeys("{tab}", 10)
        'setSendKeys("{enter}", 10)01439
        Dim SheetName As String
        SheetName = "聯盟"

        Dim args() As String = Environment.GetCommandLineArgs()

        Dim SheetNameIndex As Integer
        SheetNameIndex = args(1)
        Dim sec As Integer
        sec = args(2)
        If args(2) Is Nothing Then
            args(2) = 2
        End If
        'MsgBox("1")
        'xlsheet_sou = xlBook_sou.Worksheets(SheetName).Activate
        xlsheet_sou = xlBook_sou.Worksheets(SheetNameIndex)
        'MsgBox("2")
        Do



            'MsgBox("3")

            'MsgBox(xlBook_sou.Worksheets(SheetNameIndex).Cells(i, 1).Value)
            setInputData(xlBook_sou.Worksheets(SheetNameIndex).Cells(i, 1).Value, sec)
            i = i + 1
            'MsgBox("4")
        Loop Until xlBook_sou.Worksheets(SheetNameIndex).Cells(i, 1).Value = ""

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


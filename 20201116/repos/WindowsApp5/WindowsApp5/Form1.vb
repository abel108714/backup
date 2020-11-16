Option Strict Off
Option Explicit On
Imports System.Threading
Imports System.Drawing
Imports System.Drawing.Imaging
Imports Microsoft.VisualBasic.ApplicationServices.BuiltInRole
Imports Microsoft.VisualBasic.ApplicationServices
Imports System.IO
Imports System.Diagnostics
Imports System.ComponentModel
Imports System.Runtime.InteropServices

Public Class Form1
    'Inherits System.Web.UI.
    Inherits System.Windows.Forms.Form

    Private Structure POINTAPI
        Dim x As Integer
        Dim y As Integer
    End Structure

    Private Structure RECT
        Dim Left_Renamed As Integer
        Dim Top_Renamed As Integer
        Dim Right_Renamed As Integer
        Dim Bottom_Renamed As Integer
    End Structure

    Private Structure WINDOWPLACEMENT
        Dim Length As Integer
        Dim flags As Integer
        Dim showCmd As Integer
        Dim ptMinPosition As POINTAPI
        Dim ptMaxPosition As POINTAPI
        Dim rcNormalPosition As RECT
    End Structure

    Private Enum WinMode
        Normal = 1 ' 一般
        Maxmize = 3 ' 最大
        Minimize = 6 ' 最小
    End Enum

    Private Const SW_SHOWMINIMIZED As Short = 2
    Private Const SW_SHOWMAXIMIZED As Short = 3
    Private Const SW_SHOWNORMAL As Short = 1

    Private Declare Function SetWindowPlacement Lib "user32" (ByVal hwnd As Integer, ByRef lpwndpl As WINDOWPLACEMENT) As Integer
    Private Declare Function GetWindowPlacement Lib "user32" (ByVal hwnd As Integer, ByRef lpwndpl As WINDOWPLACEMENT) As Integer
    Private Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As Integer) As Integer


    Private Declare Function BlockInput Lib "user32" _
        (ByVal fBlock As Integer) As Integer
    Declare Auto Function SetCursorPos Lib "user32" (ByVal x As Integer, ByVal y As Integer) As Integer
    Declare Sub mouse_event Lib "user32" (ByVal dwFlags As Integer, ByVal dx As Integer, ByVal dy As Integer, ByVal dwData As Integer, ByVal dwExtraInfo As Integer)

    Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Integer
    Declare Function FindWindowEx Lib "user32" Alias "FindWindowExA" _
    (ByVal hWndParent As Integer, ByVal hWndChildAfter As Integer, ByVal lpClassName As String, ByVal lpWindowName As String) As Integer
    'Public Declare Unicode Function FindWindowW Lib "User32.dll" (ByVal className As String, ByVal windowTitle As String) As Int32

    Private Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As IntPtr) As Long

    Public Const MOUSEEVENTF_LEFTDOWN = &H2
    Public Const MOUSEEVENTF_LEFTUP = &H4
    Public Const MOUSEEVENTF_MIDDLEDOWN = &H20
    Public Const MOUSEEVENTF_MIDDLEUP = &H40
    Public Const MOUSEEVENTF_RIGHTDOWN = &H8
    Public Const MOUSEEVENTF_RIGHTUP = &H10
    Public Const MOUSEEVENTF_MOVE = &H1
    Dim a As New Process




    Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
    Public Declare Unicode Function FindWindowW Lib "User32.dll" (ByVal className As String, ByVal windowTitle As String) As IntPtr

    Private SPI_SETSCREENSAVERACTIVE As Integer = 17
    Private SPIF_SENDWININICHANGE As Integer = 2


    '<DllImport("user32", CharSet:=CharSet.Auto)>
    <DllImport("user32.dll", SetLastError:=True, CharSet:=CharSet.Auto)>
    Public Shared Function SystemParametersInfo(
        ByVal intAction As Integer,
        ByVal intParam As Integer,
        ByVal strParam As String,
        ByVal intWinIniFlag As Integer) As Integer
    End Function
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load


        Dim xlApp_sou As Object
        Dim xlBook_sou As Object
        Dim xlApp As Object
        Dim xlBook As Object
        Dim xlsheet As Object
        Dim file_dir As String
        Dim file_dir2 As String

        Me.KeyPreview = True ' HOT KEY


        Me.Visible = False

        'Me.Show()
        '238 370 按確定


        '(依路徑)自動按巨集，原檔存至(依路徑)S槽
        '\

        'Set objShell = New Shell
        'objshell.MinimizeAll
        '(0)開啟巨集
        file_dir = "C:\Users\udev77\Desktop\門市部產出報表\門市部日報表_巨集20200605新版.xls"
        file_dir2 = "S:\網通部\◎資訊\data\績效資料\Book1.xlsm"

        xlApp_sou = CreateObject("Excel.Application") '創建EXCEL應用類
        xlApp_sou.Visible = True '設置EXCEL可見



        xlBook_sou = xlApp_sou.Workbooks.Open(file_dir) '打開巨集
        Ctrl_Win_State("excel", WinMode.Maxmize) '放大視窗
        '(1)自動按巨集
        Thread.Sleep(2000)
        SetCursorPos(238, 370)
        setMouseClick("left", 2)

        Thread.Sleep(10000)
        SendKeys.SendWait("{enter}")
        Thread.Sleep(2000)
        'Dim hwd1 As IntPtr
        'hwd1 = FindWindowW(vbNullString, "門市部日報表_巨集20200605新版") '非xls  用指令聚焦
        'SetForegroundWindow(hwd1)
        'If hwd1.Equals(IntPtr.Zero) Then
        ' MsgBox("找不到")
        ' Else
        ' MsgBox("找到了1")
        ' End If


        xlsheet = xlBook_sou.Worksheets(2) '打開EXCEL第3頁工作表
        xlsheet.Activate '啟動第一頁工作表
        '30,200,0,0,708,456 門市部日報表
        '29,200,0,0,1228,499 門市部日報表(大)
        '組截圖檔名的字串
        'ex: 門市部日報表20200713_1.jpg
        'ex: 門市部日報表20200713_2.jpg
        Dim thisDate1 As Date = DateTime.Now.AddDays(-1) '前一天
        Dim report_path As String
        Dim github_report_path As String
        Dim report1 As String
        Dim report2 As String
        Dim report3 As String
        Dim report4 As String
        Dim report5 As String
        Dim report6 As String
        'Dim report7 As String
        report_path = "S:\網通部\◎資訊\"
        github_report_path = "S:\網通部\◎資訊\" & "test\"
        report1 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "1.jpg"
        report2 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "2.jpg"
        report3 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "3.jpg"
        report4 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "4.jpg"
        report5 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "5.jpg"
        report6 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "6.jpg"
        'report7 = "門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "7.jpg"
        'setScreenPic(report_path, report1, 30, 200, 0, 0, 708, 456)
        'setScreenPic(github_report_path, report1, 30, 200, 0, 0, 708, 456)


        'xlApp = CreateObject("Excel.Application") '創建EXCEL應用類
        'xlApp.Visible = True '設置EXCEL可見
        xlBook = xlApp_sou.Workbooks.Open(file_dir2) '打開報表巨集
        'xlsheet = xlBook_sou.Worksheets(2) '打開EXCEL第3頁工作表
        xlsheet.Activate '啟動第一頁工作表

        'xlApp_sou.Run("'Book1.xlsm'!調整報表符合至螢幕大小1")
        'Ctrl_Win_State("excel", WinMode.Minimize)
        'xlsheet = xlBook_sou.Worksheets(3) '打開EXCEL第3頁工作表
        'xlsheet.Activate '啟動第一頁工作表
        xlsheet = xlBook_sou.Worksheets(2) '打開EXCEL第3頁工作表
        xlsheet.Activate '啟動第一頁工作表

        'xlApp_sou.Run("'Book1.xlsm'!調整報表符合至螢幕大小2")
        'setScreenPic(report_path, report2, 29, 200, 0, 0, 1228, 499)
        'setScreenPic(github_report_path, report2, 29, 200, 0, 0, 1228, 499)

        '23,22,0,0,1153,545 基本責任業績
        '34,202,0,0,1226,301 承諾目標A
        '34,202,0,0,1226,252 承諾目標B
        '34,202,0,0,1226,351 承諾目標C
        '34,552,0,0,1226,351 承諾目標D


        '關閉螢幕保護程式
        SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 0, Nothing, SPIF_SENDWININICHANGE)
        '門市累績業績截圖
        '承諾目標A截圖
        '承諾目標B截圖
        '承諾目標C截圖
        '承諾目標D截圖
        xlApp_sou.Run("'Book1.xlsm'!門市部日報表截圖")
        'setScreenPic(report_path, report1, 34, 205, 0, 0, 1131, 727) '原本範圍
        'setScreenPic(report_path, report1, 34, 205, 0, 0, 1170, 727) '增加位數增加範圍
        'setScreenPic(github_report_path, report1, 34, 205, 0, 0, 1131, 727)
        setScreenPic(github_report_path, report1, 23, 194, 0, 0, 740, 430)
        xlApp_sou.Run("'Book1.xlsm'!承諾目標")
        xlApp_sou.Run("'Book1.xlsm'!門市累積業績截圖")
        'setScreenPic(report_path, report2, 23, 228, 0, 0, 1153, 545)
        'setScreenPic(github_report_path, report2, 23, 228, 0, 0, 1153, 545)
        setScreenPic(github_report_path, report2, 20, 191, 0, 0, 865, 443)
        xlApp_sou.Run("'Book1.xlsm'!承諾目標A截圖")
        'setScreenPic(report_path, report3, 34, 202, 0, 0, 1226, 301)
        'setScreenPic(github_report_path, report3, 34, 202, 0, 0, 1226, 301)
        setScreenPic(github_report_path, report3, 26, 195, 0, 0, 930, 229)
        xlApp_sou.Run("'Book1.xlsm'!承諾目標B截圖")
        'setScreenPic(report_path, report4, 34, 202, 0, 0, 1226, 252)
        'setScreenPic(github_report_path, report4, 34, 202, 0, 0, 1226, 252)
        setScreenPic(github_report_path, report4, 26, 195, 0, 0, 930, 191)
        xlApp_sou.Run("'Book1.xlsm'!承諾目標C截圖")
        'setScreenPic(report_path, report5, 34, 202, 0, 0, 1226, 351)
        'setScreenPic(github_report_path, report5, 34, 202, 0, 0, 1226, 351)
        setScreenPic(github_report_path, report5, 26, 195, 0, 0, 930, 267)
        xlApp_sou.Run("'Book1.xlsm'!承諾目標D截圖")
        'setScreenPic(report_path, report6, 34, 552, 0, 0, 1226, 351)
        'setScreenPic(github_report_path, report6, 34, 552, 0, 0, 1226, 351)
        setScreenPic(github_report_path, report6, 26, 423, 0, 0, 930, 267)

        '關閉
        'xlApp_sou.Run("'Book1.xlsm'!closeAllWorkbook")



        '上傳
        Dim cmd_test As Cmd = New Cmd()
        cmd_test.cmd("cd /d S:\網通部\◎資訊\")
        cmd_test.cmd("copy " & report1 & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("copy " & report2 & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("copy " & report3 & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("copy " & report4 & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("copy " & report5 & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("copy " & report6 & " " & "S:\網通部\◎資訊\test\")
        'cmd_test.cmd("copy " & report7 & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("cd /d S:\網通部\◎資訊\test\")
        cmd_test.cmd("git init") '避免git斷線
        'cmd_test.cmd("git pull") '先跟雲端同步避免git push被拒絕
        cmd_test.cmd("git add .")
        cmd_test.cmd("git commit -m " & Chr(34) & "New file" & Chr(34))
        cmd_test.cmd("git push")
        '關閉
        'cmd_test.cmd("taskkill /f /im excel.exe") 'cmd.exe /k cd S:\網通部\◎資訊\test\ & taskkill /f /im excel.exe
        Dim Procs() As Process
        Procs = System.Diagnostics.Process.GetProcessesByName("EXCEL")
        For Each a As Process In Process.GetProcesses
            If a.ProcessName = "EXCEL" Then
                a.Kill()
            End If
        Next
        'cmd_test.cmd("taskkill /f /im 自動啟動門市部產出報表小工具.exe")


        '開啟螢幕保護程式
        SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 1, Nothing, SPIF_SENDWININICHANGE)

        Me.Close()



    End Sub

    Private Sub Form1_Activated(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Activated
        Me.Visible = False
    End Sub

    Private Sub Form1_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown
        Label1.Text = e.KeyCode
    End Sub

    Protected Sub setScreenPic(pathname As String, filename As String, x As Integer, y As Integer, x1 As Integer, y1 As Integer, x2 As Integer, y2 As Integer)

        Me.Opacity = 0 '視窗透明

        ' 取得螢幕的解析度
        Dim scrnWidth As Integer = Screen.PrimaryScreen.Bounds.Width
        Dim scrnHeight As Integer = Screen.PrimaryScreen.Bounds.Height

        ' 建立Bitmap物件
        'Dim bmScrn As New Bitmap(scrnWidth, scrnHeight, PixelFormat.Format32bppArgb)
        Dim bmScrn As New Bitmap(x2, scrnHeight, PixelFormat.Format32bppArgb)
        'Dim bmScrn As New Bitmap(x2, y2, PixelFormat.Format32bppArgb)

        ' 將螢幕畫面複製到Bitmap物件中
        Dim g As Graphics = Graphics.FromImage(bmScrn)

        g.CopyFromScreen(x, y, x1, y1, New Size(x2, y2)) '設定掃瞄範圍
        g.Dispose()

        'Dim filename As String
        'Dim pathname As String
        'Dim local_path As String
        'Dim github_path As 
        'Dim filename2 As String

        Dim hwd1 As IntPtr
        hwd1 = FindWindow(vbNullString, "WindowsApp5") '聚焦視窗

        Try
            'pathname = "S:\網通部\◎資訊\"
            'filename = $"{pathname}screen_{x}_{y}_{x1}_{y1}_{x2}_{y2}.jpg"

            filename = pathname & filename & ".jpg"
            bmScrn.Save(filename) '儲存檔案

            Dim IOStm As IO.Stream = New IO.FileStream(filename, IO.FileMode.Open)
            PictureBox1.Image = New Bitmap(IOStm) '載入圖檔到視窗
            PictureBox1.SizeMode = PictureBoxSizeMode.AutoSize '自動符合視窗大小
            IOStm.Close()
        Catch ex As Runtime.InteropServices.ExternalException
            MsgBox("輸出路徑權限不足")
        End Try
        Me.Opacity = 70 '視窗透明恢復70

    End Sub

    Sub CMD_VBA_Script()
        'Shell("cmd.exe /K echo Hello World! & color 0a", vbNormalFocus)

    End Sub

    Protected Sub Button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Button1.Click

        'Me.Visible = False
        Me.Opacity = 0 '視窗透明
        ' 取得螢幕的解析度
        Dim scrnWidth As Integer = Screen.PrimaryScreen.Bounds.Width ' - 500
        Dim scrnHeight As Integer = Screen.PrimaryScreen.Bounds.Height ' - 400

        ' 建立Bitmap物件
        Dim bmScrn As New Bitmap(scrnWidth, scrnHeight, PixelFormat.Format32bppArgb)

        ' 將螢幕畫面複製到Bitmap物件中
        Dim g As Graphics = Graphics.FromImage(bmScrn)
        Dim x As Integer = 0
        Dim y As Integer = 0
        Dim x1 As Integer = 0
        Dim y1 As Integer = 0
        Dim x2 As Integer = scrnWidth
        Dim y2 As Integer = scrnHeight
        'If TextBox1.Text <> "" Then
        '    x = TextBox1.Text
        'End If
        'If TextBox2.Text <> "" Then
        '    y = TextBox2.Text
        'End If
        'If TextBox3.Text <> "" Then
        '    x1 = TextBox3.Text
        'End If
        'If TextBox4.Text <> "" Then
        '    y1 = TextBox4.Text
        'End If
        'If TextBox5.Text <> "" Then
        '    x2 = TextBox5.Text
        'End If
        'If TextBox6.Text <> "" Then
        '    y2 = TextBox6.Text
        'End If
        'g.CopyFromScreen(x, y, 0, 0, New Size(scrnWidth, scrnHeight))
        g.CopyFromScreen(x, y, x1, y1, New Size(x2, y2))
        'Dim sizex As Size = My.Computer.Screen.Bounds.Size
        'g.CopyFromScreen(New Point(0, 200), New Point(0, 200), sizex)   '截圖座標
        '設定偏移座標、設定原點座標
        g.Dispose()

        ' 儲存螢幕影像
        'If Not User.IsInRole(Administrator) Then
        'MsgBox("請以系統管理員身分執行此程式")
        'Else
        'bmScrn.Save("S:\網通部\◎資訊\screen.jpg")
        'bmScrn.Save("C:\screen.jpg")
        'End If
        Dim filename As String
        Dim hwd1 As IntPtr
        hwd1 = FindWindow(vbNullString, "WindowsApp4")

        If hwd1.Equals(IntPtr.Zero) Then
            'Label1.Text = "找不到"
            'MsgBox("找不到")
        Else
            'Label1.Text = "找到了"
            'MsgBox("找到了")
            'SetForegroundWindow(hwd1)
            'hwd2 = FindWindowEx(hwd1, 0&, "Edit", vbNullString) '內容的視窗類別是Edit
            'If hwd2.Equals(IntPtr.Zero) Then
            ' Label2.Text = "找不到"
            ' Else
            ' Label2.Text = "找到了"
            ' End If

        End If
        Try
            filename = "S:\網通部\◎資訊\screen" & "_" & x & "_" & y & ".jpg"
            bmScrn.Save(filename)
            'bmScrn.Save("C:\screen.jpg")
            Dim IOStm As IO.Stream = New IO.FileStream(filename, IO.FileMode.Open)
            PictureBox1.Image = New Bitmap(IOStm)
            PictureBox1.SizeMode = PictureBoxSizeMode.AutoSize
            IOStm.Close()
        Catch ex As Runtime.InteropServices.ExternalException
            MsgBox("輸出路徑權限不足")
        End Try
        Me.Opacity = 70 '視窗透明70
        'Me.Close()



        'Dim myImage As New Bitmap(1024, 768)
        'Dim myImage2 As New Bitmap(1280, 1024)
        'Dim g = Graphics.FromImage(myImage2)
        'g.CopyFromScreen(New Point(0, 0), New Point(0, 0), New Size(1024, 768))
        'g.CopyFromScreen(New Point(0, 0), New Point(0, 0), New Size(1280, 1024))
        'Dim dc1 As IntPtr = g.GetHdc
        'g.ReleaseHdc(dc1)
        'g.Dispose()
        'myImage2.Save("S:\網通部\◎資訊\screen2.jpg")
        'myImage2.Save("C:\\screen.jpg")
        'myImage2.Save("S:\screen.jpg")
        'myImage2.Save("S:\\screen.jpg")
    End Sub

    Function CopyScreenWithMouse() As Bitmap
        Dim b As Bitmap =
            New Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height)
        Dim g As Graphics = Graphics.FromImage(b)
        g.CopyFromScreen(New Point(0, 0), New Point(0, 0), Screen.PrimaryScreen.Bounds.Size)
        Cursor.Draw(g, New Rectangle(Cursor.Position, Cursor.Size))
        g.Dispose()
        Return b
    End Function

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

    Private Sub Form_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown
        Select Case e.KeyCode
            Case Keys.F10
                Me.Close()
            Case Keys.Enter
                Button1_Click(Button1, New System.EventArgs()) '自動按下按鈕
        End Select
    End Sub

    Private Sub Ctrl_Win_State(ByRef strWin As String, ByRef mode As WinMode)
        Dim intWnd As Integer
        Dim CurWinP As WINDOWPLACEMENT
        Dim p() As Process = System.Diagnostics.Process.GetProcessesByName(strWin)
        'MsgBox(p.Length)
        If p.Length > 0 Then '1
            intWnd = p(0).MainWindowHandle
            GetWindowPlacement(intWnd, CurWinP)
            CurWinP.Length = Len(CurWinP)
            CurWinP.flags = 0
            CurWinP.showCmd = mode
            SetWindowPlacement(intWnd, CurWinP)
            SetForegroundWindow(intWnd)
        Else '0
            intWnd = FindWindow(vbNullString, strWin)
            If intWnd.Equals(IntPtr.Zero) Then
                Exit Sub
            Else
                GetWindowPlacement(intWnd, CurWinP)
                CurWinP.Length = Len(CurWinP)
                CurWinP.flags = 0
                CurWinP.showCmd = mode
                SetWindowPlacement(intWnd, CurWinP)
                SetForegroundWindow(intWnd)
            End If
        End If
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
        'oStartInfo.WindowStyle = ProcessWindowStyle.Hidden
        'oStartInfo.CreateNoWindow = True '不顯示視窗
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

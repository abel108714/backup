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


    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load


        Dim xlApp_sou As Object
        Dim xlBook_sou As Object
        'Dim xlApp As Object
        Dim xlBook As Object
        Dim xlsheet As Object
        Dim file_dir As String
        Dim file_dir2 As String
        Dim macro_dir As String

        Me.KeyPreview = True ' HOT KEY


        Me.Visible = False

        'Me.Show()
        '238 370 按確定


        '(依路徑)自動按巨集，原檔存至(依路徑)S槽
        '\

        'Set objShell = New Shell
        'objshell.MinimizeAll
        '(0)開啟巨集
        'file_dir = "C:\Users\udev77\Desktop\門市部產出報表\門市部日報表_巨集20200605新版.xls"
        'file_dir2 = "S:\網通部\◎資訊\data\績效資料\Book1.xlsm"
        'Dim xlApp_sou As Object
        'Dim xlBook_sou As Object
        'Dim xlsheet_sou As Object
        'Dim xlApp As Object
        'Dim xlBook As Object
        'Dim xlsheet As Object
        'Dim str As Array
        'Dim fileReader As String
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim NowDate As Date = DateTime.Now

        'macro_dir = "S:\網通部\◎資訊\data\績效資料\Book1.xlsm"

        'xlApp_sou = CreateObject("Excel.Application") '創建EXCEL應用類
        'xlApp_sou.Visible = True '設置EXCEL可見
        'S:\網通部\網通部資料暫存區\★網通部績效★\20200916網通目標達成比.xlsx
        file_dir = "S:\網通部\網通部資料暫存區\★網通部績效★\" + NowDate.ToString("yyyyMMdd") + "網通目標達成比.xlsm"
        'file_dir2 = "S:\開發部\◆業績資料\2020年達成比\202010\" + NowDate.ToString("yyyyMMdd") + "實體通路目標達成比.xlsm"
        file_dir2 = "S:\網通部\◎資訊\目標達成比\實體通路\" + NowDate.ToString("yyyyMMdd") + "實體通路目標達成比.xlsm"
        'xlBook_sou = xlApp_sou.Workbooks.Open(macro_dir) '打開巨集
        'Ctrl_Win_State("excel", WinMode.Maxmize) '放大視窗
        'xlBook = Nothing
        'xlBook = xlApp_sou.Workbooks.Open(file_dir) '打開EXCEL工作簿
        'xlsheet = xlBook_sou.Worksheets(2) '打開EXCEL第2頁工作表
        'xlsheet.Activate '啟動第一頁工作表

        'S:\開發部\◆業績資料\2020年達成比\20201



        Dim report_path As String = ""
        Dim github_report_path As String = ""
        Dim report As String
        Dim report2 As String

        report_path = "S:\網通部\◎資訊\"
        github_report_path = "S:\網通部\◎資訊\" & "test\"
        report = NowDate.ToString("MM") & "01_" & NowDate.ToString("MMdd") & "網通目標達成比"
        report2 = NowDate.ToString("yyyyMMdd") + "實體通路目標達成比"
        'report_path = "S:\網通部\◎資訊\"
        'S:\網通部\◎資訊\目標達成比\實體通路
        'github_report_path = "S:\網通部\◎資訊\目標達成比\實體通路\"
        'setScreenPic(report_path, report, 20, 193, 0, 0, 999, 578) '23,196,0,0,1225,697網通報表
        'setScreenPic(github_report_path, report, 20, 193, 0, 0, 999, 578) '23,196,0,0,1225,697網通報表
        'setScreenPic(report_path, report, 20, 193, 0, 0, 999, 612) '23,196,0,0,1225,697網通報表多一列
        'setScreenPic(github_report_path, report, 20, 193, 0, 0, 999, 612) '23,196,0,0,1225,697網通報表多一列(螢幕1)
        'setScreenPic(github_report_path, report, 15, 191, 0, 0, 714, 433) '螢幕2
        setScreenPic(github_report_path, report, 15, 191, 0, 0, 715, 457) '螢幕2
        'setScreenPic(report_path2, report2, 15, 192, 0, 0, 1224, 330)
        'setScreenPic(github_report_path, report2, 15, 192, 0, 0, 1224, 330)




        '上傳
        Dim cmd_test As Cmd = New Cmd()
        cmd_test.cmd("cd /d S:\網通部\◎資訊\test")
        cmd_test.cmd("copy " & report & " " & "S:\網通部\◎資訊\test\")
        cmd_test.cmd("cd /d S:\網通部\◎資訊\test\")
        cmd_test.cmd("git init")
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

        'Dim process As New System.Diagnostics.Process()
        'Process.StartInfo.FileName = "cmd.exe"
        'Process.StartInfo.UseShellExecute = False
        'Process.StartInfo.RedirectStandardInput = True
        'Process.StartInfo.RedirectStandardOutput = True
        'Process.StartInfo.RedirectStandardError = True
        'Process.StartInfo.CreateNoWindow = True
        'Process.Start()
        'process.StandardInput.WriteLine("cd " & github_report_path & "123>test.txt") '執行指定的命令 
        'process.StandardInput.WriteLine(github_report_path & "門市部日報表20200720_2.jpg")
        'process.StandardInput.WriteLine("S:\網通部\◎資訊\test\門市部日報表20200720_2.jpg")
        'Shell("cmd.exe S:\網通部\◎資訊\test\門市部日報表20200720_2.jpg")
        'CMD_VBA_Script()
        'MsgBox("ScreenPic OK")
        'xlApp.Run("'Book1.xlsm'!調整報表符合至螢幕大小")
        '打開另存xls檔巨集(略)
        '
        'xlBook = xlApp_sou.Workbooks.Open(file_dir) '打開報表


        'MsgBox(mydocpath)




        'MsgBox("門市部日報表" & thisDate1.ToString("yyyyMMdd") & "_" & "*.xls")


        Me.Close()


    End Sub




    Private Sub Form1_Activated(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Activated
        Me.Visible = False
    End Sub

    Private Sub Form1_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown
        'Label1.Text = e.KeyCode
    End Sub

    Protected Sub setScreenPic(pathname As String, filename As String, x As Integer, y As Integer, x1 As Integer, y1 As Integer, x2 As Integer, y2 As Integer)

        Me.Opacity = 0 '視窗透明

        ' 取得螢幕的解析度
        Dim scrnWidth As Integer = Screen.PrimaryScreen.Bounds.Width
        Dim scrnHeight As Integer = Screen.PrimaryScreen.Bounds.Height

        ' 建立Bitmap物件
        'Dim bmScrn As New Bitmap(scrnWidth, scrnHeight, PixelFormat.Format32bppArgb) '這行會有空白
        Dim bmScrn As New Bitmap(x2, y2)

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
        hwd1 = FindWindow(vbNullString, "OCReportUpLoad") '聚焦視窗

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
        'Me.Opacity = 70 '視窗透明恢復70


    End Sub

    Sub CMD_VBA_Script()
        'Shell("cmd.exe /K echo Hello World! & color 0a", vbNormalFocus)

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
                'Button1_Click(Button1, New System.EventArgs()) '自動按下按鈕
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

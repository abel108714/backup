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




        Me.KeyPreview = True ' HOT KEY


        Me.Visible = False


        'Dim hwd1 As IntPtr
        'hwd1 = FindWindowW(vbNullString, "門市部日報表_巨集20200605新版") '非xls  用指令聚焦
        'SetForegroundWindow(hwd1)
        'If hwd1.Equals(IntPtr.Zero) Then
        ' MsgBox("找不到")
        ' Else
        ' MsgBox("找到了1")
        ' End If


        '30,200,0,0,708,456 門市部日報表
        '29,200,0,0,1228,499 門市部日報表(大)
        '組截圖檔名的字串
        'ex: 門市部日報表20200713_1.jpg
        'ex: 門市部日報表20200713_2.jpg
        Dim thisDate1 As Date = DateTime.Now.AddDays(-1) '前一天


        'Dim report7 As String

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


        '關閉
        'xlApp_sou.Run("'Book1.xlsm'!ST.closeAllWorkbook")



        '上傳
        Dim cmd_test As Cmd = New Cmd()
        cmd_test.cmd("cd /d S:\網通部\◎資訊\test\")
        cmd_test.cmd("git init") '避免git斷線
        'cmd_test.cmd("git pull") '先跟雲端同步避免git push被拒絕
        cmd_test.cmd("git add .")
        cmd_test.cmd("git commit -m " & Chr(34) & "New file" & Chr(34))
        cmd_test.cmd("git push")
        '關閉
        'cmd_test.cmd("taskkill /f /im excel.exe") 'cmd.exe /k cd S:\網通部\◎資訊\test\ & taskkill /f /im excel.exe

        'cmd_test.cmd("taskkill /f /im 自動啟動門市部產出報表小工具.exe")


        '開啟螢幕保護程式
        SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 1, Nothing, SPIF_SENDWININICHANGE)

        Me.Close()



    End Sub

    Private Sub Form1_Activated(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Activated
        Me.Visible = False
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

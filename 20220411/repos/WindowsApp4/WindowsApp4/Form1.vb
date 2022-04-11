Imports System.Drawing.Imaging

Public Class Form1
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

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.KeyPreview = True ' HOT KEY
        CopyScreenWithMouse()

    End Sub
    Protected Sub Button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Button1.Click

        Me.Opacity = 0 '視窗透明

        ' 取得螢幕的解析度
        Dim scrnWidth As Integer = Screen.PrimaryScreen.Bounds.Width
        Dim scrnHeight As Integer = Screen.PrimaryScreen.Bounds.Height

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
        If TextBox1.Text <> "" Then
            x = TextBox1.Text
        End If
        If TextBox2.Text <> "" Then
            y = TextBox2.Text
        End If
        If TextBox3.Text <> "" Then
            x1 = TextBox3.Text
        End If
        If TextBox4.Text <> "" Then
            y1 = TextBox4.Text
        End If
        If TextBox5.Text <> "" Then
            x2 = TextBox5.Text
        End If
        If TextBox6.Text <> "" Then
            y2 = TextBox6.Text
        End If

        g.CopyFromScreen(x, y, x1, y1, New Size(x2, y2)) '設定掃瞄範圍
        g.Dispose()

        Dim filename As String
        Dim pathname As String
        Dim hwd1 As IntPtr
        hwd1 = FindWindow(vbNullString, "WindowsApp4") '聚焦視窗

        Try
            pathname = "S:\網通部\◎資訊\"
            filename = $"{pathname}screen_{x}_{y}_{x1}_{y1}_{x2}_{y2}.jpg"
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

    Function CopyScreenWithMouse() As Bitmap
        Dim b As Bitmap =
            New Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height)
        Dim g As Graphics = Graphics.FromImage(b)
        g.CopyFromScreen(New Point(0, 0), New Point(0, 0), Screen.PrimaryScreen.Bounds.Size)
        Cursor.Draw(g, New Rectangle(Cursor.Position, Cursor.Size))
        g.Dispose()
        Return b
    End Function

    Private Sub Form_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown
        Select Case e.KeyCode
            Case Keys.F10
                Me.Close()
            Case Keys.Enter
                Button1_Click(Button1, New System.EventArgs()) '自動按下按鈕
        End Select
    End Sub

End Class

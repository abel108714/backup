Imports System.Runtime.InteropServices

Public Class Form1
    <DllImport("user32.dll", SetLastError:=True, CharSet:=CharSet.Auto)>
    Public Shared Function SystemParametersInfo(
        ByVal intAction As Integer,
        ByVal intParam As Integer,
        ByVal strParam As String,
        ByVal intWinIniFlag As Integer) As Integer
    End Function

    Private SPI_SETSCREENSAVERACTIVE As Integer = 17
    Private SPIF_SENDWININICHANGE As Integer = 2

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.Text = "螢幕保護程式控制"
        Me.Width = 397
        Me.Height = 395
        Button1.Width = 141
        Button1.Height = 55
        Button2.Width = 141
        Button2.Height = 55
        Label1.Location = New System.Drawing.Point((ClientSize.Width - Button1.Width) \ 2,
                             (ClientSize.Height - Button1.Height) * 0.5 / 3)
        Button1.Location = New System.Drawing.Point((ClientSize.Width - Button1.Width) \ 2,
                             (ClientSize.Height - Button1.Height) * 1 / 3)
        Button2.Location = New System.Drawing.Point((ClientSize.Width - Button1.Width) \ 2,
                             (ClientSize.Height - Button1.Height) * 2 / 3)
        Label1.Text = ""
        Button1.Text = "關閉螢幕保護程式"
        Button2.Text = "開啟螢幕保護程式"
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle '固定視窗大小
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        '關閉螢幕保護程式
        SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 0, Nothing, SPIF_SENDWININICHANGE)
        Label1.Text = "已關閉螢幕保護"
        'Button1不可按,Button2可按
        Button1.Enabled = False
        Button2.Enabled = True
        '關閉本程式
        Application.Exit()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        '開啟螢幕保護程式
        SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 1, Nothing, SPIF_SENDWININICHANGE)
        Label1.Text = "已開啟螢幕保護"
        'Button1可按,Button2不可按
        Button1.Enabled = True
        Button2.Enabled = False
        '關閉本程式
        Application.Exit()
    End Sub

End Class

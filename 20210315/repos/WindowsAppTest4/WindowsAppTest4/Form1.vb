
Public Class Form1
    '宣告API
    Declare Function GetCursorPos Lib "user32" Alias "GetCursorPos" (ByRef lpPoint As POINTAPI) As Integer

    Structure POINTAPI
        Dim x As Integer
        Dim y As Integer
    End Structure

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.TopMost = True
        Timer1.Enabled = True
        Timer1.Interval = 50 '每0.05秒執行一次
    End Sub

    Public now_coord As String = ""
    Dim p As POINTAPI
    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        GetCursorPos(p) '取得目前座標
        now_coord = "p.x = " & p.x & " p.y = " & p.y
        If Label1.Text <> now_coord Then '比對座標是否不同，不同就更新Label1
            Label1.Text = now_coord
            Label1.Refresh()
        End If
    End Sub

End Class

Public Class Form4
    Dim inr_num As Integer = 100
    Private Sub Form4_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ProgressBar1.Value = 0
        Label1.Text = 0 & "%"
        Me.MaximizeBox = False '關閉視窗最大化
        Me.MinimizeBox = False '關閉視窗最小化
        Me.ControlBox = False '取消關閉視窗按鈕
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle '固定視窗大小
    End Sub
    Public Sub setInrNum(i As Integer)
        inr_num = i
    End Sub
    Public Function getInrNum()
        Return inr_num
    End Function
    Public Sub setBarValue(i As Integer)
        Me.TopMost = True '最上層顯示
        ProgressBar1.Value = Math.Round((i + 1) * (100 / getInrNum()))
        Label1.Text = ProgressBar1.Value & "%"
        Label1.Refresh()
    End Sub
    Public Sub addBarValue(i As Integer)
        Me.TopMost = True '最上層顯示
        ProgressBar1.Value = ProgressBar1.Value + Math.Round((i + 1) * (100 / getInrNum()))
        Label1.Text = ProgressBar1.Value & "%"
        Label1.Refresh()
    End Sub
    Public Sub setBarValueFull()
        Me.TopMost = True '最上層顯示
        ProgressBar1.Value = 100
        Exit Sub
    End Sub
    Public Sub closeBar()
        Me.Hide()
    End Sub

End Class
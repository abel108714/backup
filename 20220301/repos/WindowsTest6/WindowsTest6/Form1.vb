Imports System.Threading
Public Class Form1
    Private Declare Function BlockInput Lib "user32" _
        (ByVal fBlock As Integer) As Integer
    Dim i As Integer = 0
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.Show()
        Me.TopMost = True
        Timer1.Enabled = True
        Timer1.Interval = 1000
        Dim first_MOUSEEVENTF As String
        Dim second_MOUSEEVENTF As String
        Dim str As String
        str = "left"
        If Equals(str, "left") Then
            MsgBox(1)
            first_MOUSEEVENTF = "MOUSEEVENTF_LEFTDOWN"
            second_MOUSEEVENTF = "MOUSEEVENTF_LEFTUP"
        ElseIf Equals(str, "middle") Then
            MsgBox(2)
            first_MOUSEEVENTF = "MOUSEEVENTF_MIDDLEDOWN"
            second_MOUSEEVENTF = "MOUSEEVENTF_MIDDLEUP"
        ElseIf Equals(str, "right") Then
            MsgBox(3)
            first_MOUSEEVENTF = "MOUSEEVENTF_RIGHTDOWN"
            second_MOUSEEVENTF = "MOUSEEVENTF_RIGHTUP"
        End If
        'MsgBox("鎖1")
        'BlockInput(True) ' 鎖
        'MsgBox("鎖2")
        'Thread.Sleep(20000) ' 等20秒
        'MsgBox("開1")
        'BlockInput(False) ' 開
        'MsgBox("開2")
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        i += 1
        Label1.Text = i & "s"
        'MsgBox(i)
        If i = 1 Then
            BlockInput(True) ' 鎖
            'MsgBox(1)

        ElseIf i = 20 Then
            BlockInput(False) ' 開
            'MsgBox(20)

        End If
    End Sub
End Class

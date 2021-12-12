Imports System.IO
Imports System.Threading
Imports System.Runtime.InteropServices


Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'MsgBox(Format(Now, "hh:mm:ss"))
        Me.Hide()
        Me.Visible = False
        SendKeys.Send("{DOWN}")
        SendKeys.SendWait("{DOWN}")
    End Sub

End Class

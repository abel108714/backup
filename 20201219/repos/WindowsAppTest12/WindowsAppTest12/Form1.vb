Imports System.Net
Imports System.Text.Encoding

Public Class Form1
    Dim publisher As New Sockets.UdpClient(0)
    Dim subscriber As New Sockets.UdpClient(2000)

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        publisher.Connect(TBTo.Text, TBPort.Text)
        Dim sendbytes() As Byte = ASCII.GetBytes(TBSend.Text)
        publisher.Send(sendbytes, sendbytes.Length)
    End Sub

    Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        Me.TopMost = True
        subscriber.Client.ReceiveTimeout = 100
        subscriber.Client.Blocking = False
        Timer1.Enabled = True
        Timer1.Interval = 100
        TBTo.Text = "172.21.7.39" '10.10.20.6    '172.21.7.39    'localhost
        TBPort.Text = "2000"
        TBSend.Text = "test"
    End Sub

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Try
            Dim ep As IPEndPoint = New IPEndPoint(IPAddress.Any, 0)
            Dim rcvbytes() As Byte = subscriber.Receive(ep)
            TBRcv.Text = ASCII.GetString(rcvbytes)
        Catch ex As Exception
        End Try
    End Sub

    Private Sub TextBox4_TextChanged(sender As Object, e As EventArgs) Handles TBRcv.TextChanged

    End Sub
End Class
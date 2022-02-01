Imports System.Net
Imports System.Net.Sockets
Imports System.Text

Module Module1

    Sub Main()

    End Sub

End Module

Public Class Form1
    Dim port As Integer = 211
    Dim udpClient As New UdpClient(port)
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.TopMost = True
        Show()
        Timer1.Enabled = True

        Timer1.Interval = 1000
        TextBox1.Text = ""
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If port <> 0 Then
            Try
                Dim RemoteIpEndPoint As New IPEndPoint(IPAddress.Any, port)

                'While (True)
                Dim receiveBytes As [Byte]() = udpClient.Receive(RemoteIpEndPoint)
                Dim receiveData As String = Encoding.UTF8.GetString(receiveBytes)
                RichTextBox1.Text = "收到資料: " & receiveData
                RichTextBox1.Text = "來自" & RemoteIpEndPoint.Address.ToString() & ":" & RemoteIpEndPoint.Port

                Dim sendData As String = "早上好, " & receiveData
                Dim sendBytes As [Byte]() = Encoding.UTF8.GetBytes(sendData)
                udpClient.Send(sendBytes, sendBytes.Length, RemoteIpEndPoint)
                RichTextBox1.Text = "傳回資料: " & sendData

                'End While
                'udpClient.Close()
            Catch ex As Exception
                RichTextBox2.Text = ex.ToString()
            End Try
        End If
    End Sub

    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        port = TextBox1.Text
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        udpClient.Close()
    End Sub
End Class

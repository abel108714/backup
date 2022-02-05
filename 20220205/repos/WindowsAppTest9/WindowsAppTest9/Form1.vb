Imports System.Net.Sockets
Imports System.Net
Imports System.Text
Imports System.Threading
Imports System.ComponentModel

Public Class Form1
    '定義兩個窗體變數
    Dim s As Socket = Nothing
    Dim t As Thread
    Dim ip As String
    Dim port As Integer
    '新建一個過程， 用於處理接收到的Socket資料包
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.TopMost = True
        Label1.Text = "ip"
        Label2.Text = "port"
        ComboBox1.Text = "10.10.20.6"
        TextBox2.Text = "1024"
        Me.Show()

    End Sub

    Public Sub setSocket(ip As String, port As Integer)
        Me.ip = ip
        Me.port = port
    End Sub

    Public Function getSocketIP()
        Return ip
    End Function

    Public Function getSocketPORT()
        Return port
    End Function

    Public Sub WaitData()
        s = New Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp) '使用TCP協議
        'Dim localEndPoint As New IPEndPoint(IPAddress.Parse("172.21.7.39"), 1024)  '指定IP和Port
        Dim localEndPoint As New IPEndPoint(IPAddress.Parse(getSocketIP()), getSocketPORT())  '指定IP和Port
        Try
            s.Bind(localEndPoint)        '繫結到該Socket
            s.Listen(100)     '偵聽，最多接受100個連線
            While (True)
                Dim bytes(1024) As Byte   '用來儲存接收到的位元組
                Dim ss As Socket = s.Accept()  '若接收到,則建立一個新的Socket與之連線
                ss.Receive(bytes)    '接收資料，若用ss.send(Byte()),則傳送資料
                ListBox1.Items.Insert(0, Encoding.Unicode.GetString(bytes)) '將其插入到列表框的第一項之前
                '若使用Encoding.ASCII.GetString(bytes),則接收到的中文字元不能正常顯示
            End While
        Catch ex As Exception
            MsgBox(ex.ToString, 0 + 64, "錯誤訊息")
        End Try
    End Sub

    Private Sub BtnStart_Click(sender As Object, e As EventArgs) Handles BtnStart.Click
        '在BtnStart的click事件中，加入如下程式碼:
        setSocket(ComboBox1.Text, TextBox2.Text)
        t = New Thread(AddressOf WaitData)  '建立新的執行緒
        t.Start()     '啟動執行緒
        BtnStart.Enabled = False   '按鈕不可用，避免另啟執行緒
    End Sub

    Private Sub BtnStop_Click(sender As Object, e As EventArgs) Handles BtnStop.Click
        '在BtnStop的click事件中，加入如下程式碼
        Try
            s.Close()     '關閉Socket
            t.Abort()     '中止執行緒
        Catch
        Finally
            BtnStart.Enabled = True   '啟用BtnStart
        End Try
    End Sub

    Private Sub Form1_Closing(sender As Object, e As CancelEventArgs) Handles Me.Closing
        '為了防止使用者不點選Stop直接退出，而不能使執行緒結束，則應在窗體的closing事件中，加入如下程式碼
        Try
            s.Close()
            t.Abort()
        Catch
        End Try
    End Sub

    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged

    End Sub
End Class

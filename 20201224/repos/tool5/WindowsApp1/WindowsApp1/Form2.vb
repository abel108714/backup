Imports System.IO

Public Class Form2
    Dim progPath As String
    Dim dataPath As String

    Public Sub Form_Load() Handles Me.Load
        Dim str As Array
        Dim not_EOL_str As Array
        Dim fileReader As String
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\pathfile.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\pathfile.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(0), "=")
            If String.Compare(str(0), "softpath") = 0 Then
                progPath = str(1)
            End If
        Else
            'MsgBox("檔案不存在")
            progPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\EXCEL.EXE"
        End If
        TextBox1.Text = progPath

        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\pathfile.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\pathfile.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(1), "=")
            If String.Compare(str(0), "datapath") = 0 Then
                dataPath = str(1)
            End If
        Else
            'MsgBox("檔案不存在")
            dataPath = "S:\網通部\◎資訊\data\績效資料\"
        End If
        TextBox2.Text = dataPath

        Me.MaximizeBox = False '關閉視窗最大化
        Me.MinimizeBox = False '關閉視窗最小化
        Me.FormBorderStyle = Windows.Forms.FormBorderStyle.FixedSingle '固定視窗大小
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If (FolderBrowserDialog1.ShowDialog() = DialogResult.OK) Then
            TextBox1.Text = FolderBrowserDialog1.SelectedPath
        End If
    End Sub

    Private Sub Button2_Click_1(sender As Object, e As EventArgs) Handles Button2.Click
        If (FolderBrowserDialog1.ShowDialog() = DialogResult.OK) Then
            TextBox2.Text = FolderBrowserDialog1.SelectedPath
        End If
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        '儲存記錄
        Dim lines As String
        Dim soft_path As String = TextBox1.Text
        Dim data_path As String = TextBox2.Text
        '儲存內容
        lines = "softpath=" & soft_path
        lines += vbCrLf
        lines += "datapath=" & data_path
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\pathfile.txt"))
            For Each line As String In lines
                outputFile.Write(line)
            Next
        End Using
        Me.Close() '結束視窗
    End Sub

    Private Sub Form_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class
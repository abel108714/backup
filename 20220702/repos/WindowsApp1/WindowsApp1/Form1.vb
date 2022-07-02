Imports System.IO
'Imports Microsoft.Office.Interop.Excel

Public Class Form1
    Dim progPath As String
    Dim dataPath As String

    Public Sub Form_load() Handles Me.Load
        Button1.Location = New Point((ClientSize.Width - Button1.Width) \ 2,
                             (ClientSize.Height - Button1.Height) \ 2)
        ' The following statement calls the Get procedure of the Visual Basic Now property.
        Label1.Text = System.DateTime.Now
        Dim d1 As String = DateTime.Parse(Label1.Text).ToString("dd/MM/yyyy hh:mm:ss tt")
        Me.MaximizeBox = False '關閉視窗最大化
        Me.MinimizeBox = False '關閉視窗最小化
        Me.FormBorderStyle = Windows.Forms.FormBorderStyle.FixedSingle '固定視窗大小
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim xlApp As Object
        Dim xlBook As Object
        Dim xlsheet As Object
        Dim str As Array
        Dim fileReader As String
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        '讀取記錄及檢查檔案是否存在
        Dim not_EOL_str As Array
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\pathfile.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\pathfile.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(0), "=")
            If String.Compare(str(0), "softpath") = 0 Then
                progPath = str(1)
            End If
            str = Split(not_EOL_str(1), "=")
            If String.Compare(str(0), "datapath") = 0 Then
                dataPath = str(1)
            End If
        Else
            'MsgBox("檔案不存在")
        End If

        'MsgBox("The formatted date is " & Format(#5/31/1993#, "dddd, d MMM yyyy"))
        'progPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\EXCEL.EXE"
        'dataPath = root & "2020-04-08-08-40-09_N每日業績N.xls"

        Dim thisDate1 As Date = #2020/04/08#
        'MsgBox(thisDate1.ToString("yyyy-MM-dd-") & "40-09")
        dataPath = dataPath & "\" & thisDate1.ToString("yyyy-MM-dd-") & "08-40-09" _
& "_N每日業績N.xls"

        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            str = Split(fileReader, "=")
            If String.Compare(str(0), "autoCloseCheck") = 0 Then
                'MsgBox("str(1) : " & str(1))
                If str(1) = "True" Then
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
                Else
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
                End If
            End If

        Else
            'MsgBox("檔案不存在")
            '儲存內容,檔案開頭
            'lines += "----------------------"
            'lines += vbCrLf
            'lines += "System Registry Editor"
            'lines += vbCrLf
            'lines += "----------------------"
            'lines += vbCrLf
            'lines += vbCrLf
        End If

        If Dir(progPath) = "" Then '判斷EXCEL是否打開
            xlApp = CreateObject("Excel.Application") '創建EXCEL應用類
            xlApp.Visible = True '設置EXCEL可見
            xlBook = xlApp.Workbooks.Open(dataPath) '打開EXCEL工作簿
            xlsheet = xlBook.Worksheets(1) '打開EXCEL第一頁工作表
            xlsheet.Activate '啟動第一頁工作表
            xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoActivate) '運行EXCEL中的啟動宏
            xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoOpen)
            'Microsoft.Office.Interop.Excel與new Point套件衝突不能引入
            xlsheet = xlBook.Worksheets(2) '打開EXCEL第二頁工作表
            xlsheet.Activate '啟動第二頁工作表
            'MsgBox(Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked)
            If Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked Then
                Me.Close() '結束視窗
            End If
        Else
            MsgBox("EXCEL已打開")
        End If
    End Sub

    Private Sub 開啟檔案自動結束視窗ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 開啟檔案自動結束視窗ToolStripMenuItem.Click

        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim str As Array
        Dim fileReader As String
        Dim lines As String
        lines = ""
        If Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True Then
            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
        Else
            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
        End If

        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            str = Split(fileReader, "=")
            'MsgBox(String.Compare(str(0), "autoCloseCheck "))
            If String.Compare(str(0), "autoCloseCheck ") = 0 Then
                If str(1) = "True" Then
                    'Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
                Else
                    'Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
                End If
            End If
        Else
            'MsgBox("檔案不存在")
            '儲存內容,檔案開頭
            'lines += "----------------------"
            'lines += vbCrLf
            'lines += "System Registry Editor"
            'lines += vbCrLf
            'lines += "----------------------"
            'lines += vbCrLf
            'lines += vbCrLf
        End If

        '儲存內容
        lines += "autoCloseCheck=" & Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked

        '儲存記錄
        Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\autoCloseCheck.txt"))
            outputFile.Write(lines)
            str = Split(lines, "=")
            If str(0) = "autoCloseCheck" Then
                'MsgBox(str(1))
            End If
        End Using

        '讀取記錄
        fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
        'MsgBox(fileReader)
        str = Split(fileReader, "=")
        If String.Compare(str(0), "autoCloseCheck ") = 0 Then
            'MsgBox("true")
        End If

    End Sub

    Private Sub 主程式路徑ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 主程式路徑ToolStripMenuItem.Click
        Dim inputFrom As New Form2
        inputFrom.Show()
        'Me.Dispose(False)
    End Sub

    Private Sub 設定ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 設定ToolStripMenuItem.Click

        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            Dim str As Array
            Dim fileReader As String
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            str = Split(fileReader, "=")
            If String.Compare(str(0), "autoCloseCheck") = 0 Then
                If String.Compare(str(1), "True") = 0 Then
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
                Else
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
                End If
            End If
        Else
            'MsgBox("檔案不存在")
        End If
    End Sub
End Class

Imports System.Drawing.Text
Imports System.IO
Imports System.Text.RegularExpressions
Imports Microsoft.Office.Interop.Excel
'Imports Microsoft.Office.Interop.Excel
Public Class Form1
    Private Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Integer
    Dim dataPath As String
    Dim dataPath2 As String
    Dim dataPath3 As String
    Dim macroPath As String = My.Computer.FileSystem.CurrentDirectory()
    Dim progPath As String
    Dim autoCloseCheck As String
    Dim autoHideWin As String
    Public Property Listbox1 As Object
    Private Sub PrintProductVersion()
        Label2.Text = System.Windows.Forms.Application.ProductVersion
    End Sub
    Public Sub Form_load() Handles Me.Load
        Button1.Location = New System.Drawing.Point((ClientSize.Width - Button1.Width) \ 2,
                             (ClientSize.Height - Button1.Height) \ 2)
        Label1.Text = System.DateTime.Now
        Label1.Visible = False
        Dim d1 As String = DateTime.Parse(Label1.Text).ToString("dd/MM/yyyy hh:mm:ss tt")
        PrintProductVersion()
        'Me.MaximizeBox = False '關閉視窗最大化
        'Me.MinimizeBox = False '關閉視窗最小化
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle '固定視窗大小

        KeyPreview = True
        Me.KeyPreview = True ' HOT KEY

        Dim str As Array
        Dim not_EOL_str As Array
        Dim fileReader As String
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim autoHideWin As String
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(1), "=")
            If String.Compare(str(0), "autoHideWin") = 0 Then
                autoHideWin = str(1)
                If autoHideWin = "True" Then
                    Try
                        Button1_Click(Button1, New System.EventArgs()) '自動按下按鈕
                    Catch ex As Exception
                        MsgBox(ex.Message)
                    End Try
                End If
            End If
        Else
            'MsgBox("檔案不存在")
        End If

    End Sub
    Private Sub Form_resize(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Resize
        Try
            If Me.WindowState = FormWindowState.Minimized Then
                Me.Visible = False
                NotifyIcon1.Visible = True
            End If
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub
    Private Sub Form_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown
        Dim Edit_Mode As String
        Select Case e.KeyCode
            Case Keys.Escape
                Edit_Mode = "Esc"
                'MsgBox("Escape pressed")
                Me.Close()
            Case Keys.Enter
                Edit_Mode = "enter"
                'MsgBox("enter pressed")
                Button1_Click(Button1, New System.EventArgs()) '按下按鈕
            Case Keys.F1
                Edit_Mode = "F1"
                'MsgBox("F1 pressed")
                Me.Visible = False '隱藏小工具介面
                NotifyIcon1.Visible = True '左下角顯示
                Me.WindowState = FormWindowState.Minimized
        End Select
    End Sub

    Private Sub NotifyIcon1_MouseDoubleClick(ByVal sender As System.Object, ByVal e As MouseEventArgs) Handles NotifyIcon1.MouseDoubleClick
        Try
            Me.Visible = True
            Me.WindowState = FormWindowState.Normal
            NotifyIcon1.Visible = False
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub

    Private Sub 路徑設定ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 路徑設定ToolStripMenuItem.Click
        Dim inputFrom As New Form2
        inputFrom.Show()
        'Me.Dispose(False)
    End Sub

    Private Sub 離開ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 離開ToolStripMenuItem.Click
        Me.Close()
    End Sub

    Private Sub OpenToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles OpenToolStripMenuItem.Click
        'Me.ShowDialog() '最上層顯示
        Try

            Me.Visible = True
            Me.WindowState = FormWindowState.Normal
            NotifyIcon1.Visible = False
            'notifyicon1.showballoontip(1, "notifyicon", "running", tooltipicon.info)
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub

    Private Sub ExitToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ExitToolStripMenuItem.Click
        Me.Close()
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim xlApp_sou As Object
        Dim xlBook_sou As Object
        'Dim xlsheet_sou As Object
        'Dim xlApp As Object
        Dim xlBook As Object
        Dim xlsheet As Object
        Dim str As Array
        Dim fileReader As String
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        '讀取記錄及檢查檔案是否存在
        Dim not_EOL_str As Array
        'Me.Focus()
        'SendKeys.SendWait("F1")
        'Me.Visible = False '隱藏小工具介面
        'NotifyIcon1.Visible = True '左下角顯示
        Me.WindowState = FormWindowState.Minimized
        'Me.Hide()

        Dim hwd1 As IntPtr
        hwd1 = FindWindow(vbNullString, "產生開發部門業績表小工具")
        'Me.Visible = False
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
                dataPath2 = str(1)
                dataPath = str(1)
            End If
        Else
            'MsgBox("檔案不存在")
        End If

        'MsgBox("The formatted date is " & Format(#5/31/1993#, "dddd, d MMM yyyy"))
        'progPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\EXCEL.EXE"
        'dataPath = root & "2020-04-08-08-40-09_N每日業績N.xls"
        Dim thisDate1 As Date = DateTime.Now.AddDays(-1) '#2020/04/08#
        'MsgBox(thisDate1)
        'MsgBox(thisDate1.ToString("yyyy-MM-dd-") & "40-09")
        Dim str1 As String
        Dim str2 As String
        Dim str3 As String
        str1 = "2020-04-08-08-40-09_N每日業績N.xls     "
        str2 = "2020-04-08-" '1
        str3 = "_N每日業績N.xls" '20

        Dim root As String = dataPath
        dataPath2 = dataPath & "\Book1.xlsm"
        'Dim RetVal
        'RetVal = Shell("C:\WINDOWS\CALC.EXE", 1)    ' Run Calculator.
        'My.Computer.FileSystem.CopyFile(macroPath & "\網通部門業績表.xlsm", dataPath & "網通部門業績表.xlsm", overwrite:=False)
        'My.Computer.FileSystem.CopyFile(macroPath & "\網通部門業績表.bas", dataPath & "網通部門業績表.bas", overwrite:=False)
        'macroPath = dataPath & "網通部門業績表.xlsm"
        dataPath = dataPath & "\" & thisDate1.ToString("yyyy-MM-dd-") & "08-40-09" _ '"\d{4}-\d{2}-\d{2}")
& "_N每日業績N.xls"

        '讀取記錄及檢查檔案是否存在
        'MsgBox(111)
        'If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
        '    'MsgBox("檔案存在")
        '    '讀取記錄及檢查檔案是否存在
        '    MsgBox(112)
        '    fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
        '    MsgBox(113)
        '    str = Split(fileReader, "=")
        '    MsgBox(str(0))
        '    MsgBox(str(1))
        '    If String.Compare(str(0), "autoCloseCheck") = 0 Then
        '        'MsgBox("str(1) : " & str(1))
        '        If str(1) = "True" Then
        '            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
        '        Else
        '            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
        '        End If
        '    End If

        'Else
        '    'MsgBox("檔案不存在")
        '    '儲存內容,檔案開頭
        '    'lines += "----------------------"
        '    'lines += vbCrLf
        '    'lines += "System Registry Editor"
        '    'lines += vbCrLf
        '    'lines += "----------------------"
        '    'lines += vbCrLf
        '    'lines += vbCrLf
        'End If
        'Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        'Dim str As Array
        'Dim fileReader As String
        Dim lines As String
        Dim strPath As String
        lines = ""
        'Dim not_EOL_str As Array
        'Dim fileReader As String
        'Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(0), "=")
            'MsgBox(not_EOL_str(0))
            If String.Compare(str(0), "autoCloseCheck") = 0 Then
                'MsgBox(str(0))
                'MsgBox(str(1))
                autoCloseCheck = str(1)
                If str(1) = "True" Then
                    'MsgBox(0)
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
                Else
                    'MsgBox(1)
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
                End If
            End If
        Else
            'MsgBox("檔案不存在")
            'progPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\EXCEL.EXE"
            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
        End If
        'hwd1 = FindWindow(vbNullString, "產生網通部門業績表小工具")
        'Me.Visible = False
        'F1If hwd1.Equals(IntPtr.Zero) Then
        'MsgBox("該程式沒執行")
        'Else
        'MsgBox("該程式執行")
        'End If
        If Dir(progPath) = "" Then '判斷EXCEL是否打開


            '先找指定名稱
            Try
                Dim dir As String = ""
                Dim dirs As String() = Directory.GetFiles(root, thisDate1.ToString("yyyy-MM-dd-") & "*.xls")

                For Each dir In dirs
                    'MsgBox(If(File.Exists(dir), "File exists.", "File does not exist."))
                Next
                If File.Exists(dir) And dirs.Length = 1 Then
                    xlApp_sou = CreateObject("Excel.Application") '創建EXCEL應用類
                    xlApp_sou.Visible = True '設置EXCEL可見
                    xlBook_sou = xlApp_sou.Workbooks.Open(dataPath2) '打開EXCEL工作簿
                    'MsgBox(dataPath2)
                    'xlBook_sou = xlApp_sou.Workbooks.Open(macroPath) '打開EXCEL工作簿
                    'MsgBox(dataPath2)
                    'xlsheet_sou = xlBook_sou.Worksheets(1) '打開EXCEL第一頁工作表
                    'xlsheet_sou.Activate '啟動第一頁工作表
                    'xlApp_sou.Run("網通部門業績表") '第一個為sub名稱,第二個為要傳遞的參數
                    'xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoActivate) '運行EXCEL中的啟動宏
                    'xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoOpen)
                    'Microsoft.Office.Interop.Excel與new Point套件衝突不能引入
                    'xlsheet_sou = xlBook_sou.Worksheets(2) '打開EXCEL第二頁工作表
                    'xlsheet_sou.Activate '啟動第二頁工作表

                    'xlApp = CreateObject("Excel.Application") '創建EXCEL應用類
                    'xlApp.Visible = True '設置EXCEL可見
                    xlBook = xlApp_sou.Workbooks.Open(dir) '打開EXCEL工作簿
                    strPath = dir
                    'MsgBox(dir)
                    'MsgBox(dir)
                    xlsheet = xlBook.Worksheets(2) '打開EXCEL第二頁工作表
                    xlsheet.Activate '啟動第一頁工作表
                    xlApp_sou.Run("'Book1.xlsm'!Module1.開發部門業績表") '第一個為sub名稱,第二個為要傳遞的參數
                    'xlApp_sou.Run("'網通部門業績表.xlsm'!網通部門業績表")
                    'xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoActivate) '運行EXCEL中的啟動宏
                    'xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoOpen)
                    'Microsoft.Office.Interop.Excel與new Point套件衝突不能引入
                    xlsheet = xlBook.Worksheets(2) '打開EXCEL第二頁工作表
                    xlsheet.Activate '啟動第二頁工作表
                    xlApp_sou = Nothing '釋放EXCEL對象

                Else
                    '若無，讓使用者選擇
                    'MsgBox("無每日業績表或有兩個以上業績表，請另選檔案")
                    OpenFileDialog1.InitialDirectory = root
                    'MsgBox(root)
                    OpenFileDialog1.FileName = thisDate1.ToString("yyyy-MM-dd-")
                    OpenFileDialog1.Filter = "*|*.xls" '2020-04-08-08-40-09_N每日業績N.xls"
                    Dim r As Integer = OpenFileDialog1.ShowDialog()
                    If r = DialogResult.OK Then
                        xlApp_sou = CreateObject("Excel.Application") '創建EXCEL應用類
                        xlApp_sou.Visible = True '設置EXCEL可見
                        xlBook_sou = xlApp_sou.Workbooks.Open(dataPath2) '打開EXCEL工作簿
                        'MsgBox(dataPath2)
                        'xlBook_sou = xlApp_sou.Workbooks.Open(macroPath) '打開EXCEL工作簿
                        'System.Diagnostics.Process.Start(OpenFileDialog1.FileName) '執行
                        xlBook = xlApp_sou.Workbooks.Open(OpenFileDialog1.FileName) '打開EXCEL工作簿
                        strPath = OpenFileDialog1.FileName
                        'MsgBox(OpenFileDialog1.FileName)
                        'xlBook = xlApp_sou.Workbooks.Open(dir) '打開EXCEL工作簿
                        xlsheet = xlBook.Worksheets(1) '打開EXCEL第一頁工作表
                        xlsheet.Activate '啟動第一頁工作表
                        xlApp_sou.Run("'Book1.xlsm'!Module1.開發部門業績表") '第一個為sub名稱,第二個為要傳遞的參數
                        'xlApp_sou.Run("'Book1.xlsm'!網通部門業績表") '第一個為sub名稱,第二個為要傳遞的參數
                        'xlApp_sou.Run("'網通部門業績表.xlsm'!網通部門業績表")
                        'xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoActivate) '運行EXCEL中的啟動宏
                        'xlBook.RunAutoMacros(Microsoft.Office.Interop.Excel.XlRunAutoMacro.xlAutoOpen)
                        'Microsoft.Office.Interop.Excel與new Point套件衝突不能引入
                        xlsheet = xlBook.Worksheets(2) '打開EXCEL第二頁工作表
                        xlsheet.Activate '啟動第二頁工作表
                        xlApp_sou = Nothing '釋放EXCEL對象

                    End If
                End If

                'MsgBox(111)
                'MsgBox(Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked)
                If Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked Then
                    'MsgBox(123)
                    Dim autohidewin As String
                    '讀取記錄及檢查檔案是否存在
                    'MsgBox(mydocpath)
                    'MsgBox(222)
                    If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
                        'MsgBox("檔案存在")
                        'MsgBox(333)
                        fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
                        not_EOL_str = Split(fileReader, vbCrLf)
                        str = Split(not_EOL_str(1), "=")
                        If String.Compare(str(0), "autoHideWin") = 0 Then
                            'MsgBox("1")
                            autohidewin = str(1)
                            'Me.Focus()
                            'hwd1 = FindWindow(vbNullString, "產生網通部門業績表小工具")
                            'Me.Visible = False
                            'System.Windows.Forms.Application.DoEvents()
                            'Me.Refresh()
                            'If hwd1.Equals(IntPtr.Zero) Then
                            '    MsgBox("該程式沒執行")
                            'Else
                            '    MsgBox("該程式執行")
                            'End If
                            If autohidewin = "True" Then
                                'MsgBox("2")
                                Try
                                    'MsgBox("22")

                                    'Form_load()
                                    'Form1.Show()
                                    'Me.Visible = False
                                    hwd1 = FindWindow(vbNullString, "產生開發部門業績表小工具")
                                    'Me.Visible = False
                                    'System.Windows.Forms.Application.DoEvents()
                                    'Me.Refresh()
                                    If hwd1.Equals(IntPtr.Zero) Then
                                        'MsgBox("該程式沒執行")
                                    Else
                                        'MsgBox("該程式執行")
                                        'Me.WindowState = FormWindowState.Minimized
                                        'Me.Close() '結束視窗
                                        'Me.Show()
                                        'Me.Visible = False
                                        'NotifyIcon1.Visible = True '左下角顯示
                                        'System.Windows.Forms.Application.DoEvents()
                                        'Me.Refresh()
                                    End If
                                Catch ex As Exception
                                    MsgBox(ex.Message)
                                End Try
                            Else
                                'MsgBox("3")
                                'Me.Close() '結束視窗
                            End If
                        End If
                    Else
                        'msgbox("檔案不存在")
                    End If
                    'Me.Close() '結束視窗
                End If
            Catch ex As Exception
                Console.WriteLine("The process failed: {0}", ex.ToString())
            End Try

        Else
            MsgBox("EXCEL已打開")
        End If


    End Sub

    'Private Sub Form1_Activated(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Activated
    '    'Me.Visible = False
    'End Sub
    Function IsFileOpen(fileName As String) As Boolean
        On Error Resume Next
        Dim wb As Microsoft.Office.Interop.Excel.Workbook = Workbook(fileName)
        On Error GoTo 0
        If Not wb Is Nothing Then IsFileOpen = True
    End Function

    Private ReadOnly Property Workbook(fileName As String) As Workbook
        Get
            Throw New NotImplementedException()
        End Get
    End Property

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
        str = Split(fileReader, "=")
        If String.Compare(str(0), "autoCloseCheck ") = 0 Then
            'MsgBox("true")
        End If

        '儲存記錄
        'Dim lines As String
        '儲存內容
        lines = "autoCloseCheck=" & Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked
        lines += vbCrLf
        lines += "autoHideWin=" & Me.不顯示小工具介面ToolStripMenuItem.Checked
        'MsgBox(lines)
        Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\autoCloseCheck.txt"))
            For Each line As String In lines
                outputFile.Write(line)
            Next
        End Using

    End Sub

    Private Sub 設定ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 設定ToolStripMenuItem.Click
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim str As Array
        Dim fileReader As String
        Dim lines As String
        lines = ""
        'Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        '讀取記錄及檢查檔案是否存在
        'If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
        '    'MsgBox("檔案存在")
        '    'Dim str As Array
        '    'Dim fileReader As String
        '    fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
        '    str = Split(fileReader, "=")
        '    If String.Compare(str(0), "autoCloseCheck") = 0 Then
        '        If String.Compare(str(1), "True") = 0 Then
        '            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
        '        Else
        '            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
        '        End If
        '    End If
        'Else
        '    'MsgBox("檔案不存在")
        '    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
        '    '儲存內容
        '    lines += "autoCloseCheck=" & Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked
        '    '儲存記錄
        '    Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\autoCloseCheck.txt"))
        '        outputFile.Write(lines)
        '    End Using
        'End If

        Dim not_EOL_str As Array
        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(0), "=")
            If String.Compare(str(0), "autoCloseCheck") = 0 Then
                autoCloseCheck = str(1)
                If str(1) = "True" Then
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
                Else
                    Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = False
                End If
            End If
        Else
            'MsgBox("檔案不存在")
            'progPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\EXCEL.EXE"
            Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked = True
        End If

        '讀取記錄及檢查檔案是否存在
        If File.Exists(mydocpath & Convert.ToString("\autoCloseCheck.txt")) Then
            'MsgBox("檔案存在")
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\autoCloseCheck.txt"), System.Text.Encoding.UTF8)
            not_EOL_str = Split(fileReader, vbCrLf)
            str = Split(not_EOL_str(1), "=")
            If String.Compare(str(0), "autoHideWin") = 0 Then
                autoHideWin = str(1)
                If str(1) = "True" Then
                    Me.不顯示小工具介面ToolStripMenuItem.Checked = True
                Else
                    Me.不顯示小工具介面ToolStripMenuItem.Checked = False
                End If
            End If
        Else
            'MsgBox("檔案不存在")
            Me.不顯示小工具介面ToolStripMenuItem.Checked = False
        End If

    End Sub

    Private Sub 不顯示小工具介面ToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles 不顯示小工具介面ToolStripMenuItem.Click

        If Me.不顯示小工具介面ToolStripMenuItem.Checked = True Then
            Me.不顯示小工具介面ToolStripMenuItem.Checked = False
        Else
            Me.不顯示小工具介面ToolStripMenuItem.Checked = True
        End If
        '儲存記錄
        Dim lines As String
        '儲存內容
        lines = "autoCloseCheck=" & Me.開啟檔案自動結束視窗ToolStripMenuItem.Checked
        lines += vbCrLf
        lines += "autoHideWin=" & Me.不顯示小工具介面ToolStripMenuItem.Checked

        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\autoCloseCheck.txt"))
            For Each line As String In lines
                outputFile.Write(line)
            Next
        End Using
    End Sub

End Class

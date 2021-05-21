Imports System.IO
Imports System.Windows.Forms.VisualStyles.VisualStyleElement.Status

Public Class Form1

    Private count As Integer
    Dim record_Cell_0 As String = ""
    Dim record_Cell_1 As String = ""
    Dim record_row As Integer = -1
    Dim StartFlag As Boolean = False
    Dim ExceOrederIndex As Integer
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Try
            Dim period As String
            Dim Hour As String
            Dim Minute As String
            Button2.Enabled = False '按鈕停用
            Button3.Enabled = False '按鈕停用
            'Label1.Text = Format(Now, "yyyy-MM-dd hh:mm:ss")
            'Label2.Text = "順序編號"
            'Label3.Text = "啟動程式"
            'Label4.Text = "啟動時間"
            Label2.Text = "啟動程式"
            Label3.Text = "啟動時間"
            Label4.Text = ""
            Label5.Text = ""
            Label6.Text = ""
            Timer1.Enabled = True
            Timer1.Interval = 10000
            'TextBox2.Text = "C:\Users\udev77\Desktop\自動產生鼎新業績報表小工具.exe"
            'TextBox3.Text = "C:\Users\udev77\Desktop\自動啟動門市部產出報表小工具.exe"
            'C:\Users\udev77\Desktop\自動產生鼎新業績報表小工具.exe,下午 - 5:30
            'C:\Users\udev77\Desktop\自動啟動門市部產出報表小工具.exe,下午 - 5:30
            test()
            'Dim f As String = Path.GetFileName("C:\Users\udev77\Desktop\testStart.bat") '路徑取得檔名
            'MsgBox(f)
            'Dim p As String = Path.GetDirectoryName("C:\Users\udev77\Desktop\testStart.bat") '路徑取得檔名
            'MsgBox(p)
            'Dim cmd_test As Cmd = New Cmd()
            'cmd_test.cmd("cd C:\Users\udev77\Desktop\")
            'cmd_test.cmd("testStart.bat")


            For h = 0 To 23
                If h <= 11 Then
                    period = "上午 - "
                    Hour = CStr(h)
                Else
                    period = "下午 - "
                    Hour = CStr(h - 12)
                End If
                If Hour = "0" Then
                    Hour = CStr(12)
                End If
                For m = 0 To 59
                    If m < 10 Then
                        Minute = "0" & CStr(m)
                    Else
                        Minute = CStr(m)
                    End If
                    ComboBox1.Items.Add(period & Hour & ":" & Minute)
                Next
            Next

            Dim arrPro(2) As String


            '儲存記錄
            'Dim lines As String

            'Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
            '儲存內容
            'lines = TextBox1.Text
            'lines += vbCrLf

            '比對strArray(0)越小的越先執行strArray(1)的程式
            'Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
            'Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\ExecOrder.txt"))
            ' For Each line As String In lines
            ' outputFile.Write(line)
            '
            '        Next
            '        End Using

            '先把strArray(0)排序然後在指定時間strArray(2)執行

            '若時間順序早於strArray(0)則顯示紅字提醒更正

            '迴圈依讀取txt檔的指定時間陣列依序執行程式

            'Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
            'Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\ExecOrder.txt"))
            ' For Each line As String In lines
            ' outputFile.Write(line)
            ' 'MsgBox(line)
            ' Next
            ' End Using
            'Me.Close() '結束視窗
            'test()
            'MsgBox(DataGridView1.RowCount)
            'MsgBox(get24HourClock(getExecOrder(ExceOrederIndex)))

            For i As Integer = 1 To 9
                ComboBox1.Items.Add(i)
            Next
            'DataGridView1.Columns.Add("Start item No", "順序編號")
            DataGridView1.Columns.Add("Start program", "啟動程式")
            DataGridView1.Columns.Add("Start time", "啟動時間")

            'DataGridView1唯讀
            'DataGridView1.Columns("Start item No").ReadOnly = True
            DataGridView1.Columns("Start program").ReadOnly = True
            DataGridView1.Columns("Start time").ReadOnly = True

            'DataGridView1設定寬度
            'DataGridView1.Columns("Start item No").Width = 80
            'DataGridView1.Columns("Start program").Width = 275
            DataGridView1.Columns("Start program").Width = 355
            DataGridView1.Columns("Start time").Width = 125

            Dim fileReader As String
            Dim not_EOL_str As Array
            Dim strArray As Array
            Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
            fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), System.Text.Encoding.UTF8)
            Dim j As Integer = 0
            Dim k As Integer = 0
            not_EOL_str = Split(fileReader, vbCrLf)
            'While j < 10
            DataGridView1.AllowUserToAddRows = False '刪除預設空白列
            For k = 0 To not_EOL_str.Length
                strArray = Split(not_EOL_str(k), ",")
                DataGridView1.Rows.Add(New Object() {strArray(0), strArray(1)})
            Next
            'DataGridView1.Refresh()
            '    j = j + 1
            'End While

            'Shell("cmd.exe")
            'MsgBox(getDataRowCount())
        Catch ex As Exception

        End Try
        'MsgBox(DataGridView1.RowCount)
        'MsgBox(getOrderCt())
        '讀取時間到陣列


        Dim TimeArr As Array = Nothing
        Dim t As Integer
        MsgBox(get24HourClock("上午 - 12:00"))
        For t = 0 To getOrderCt() - 1
            Try
                TimeArr(t) = getExecOrder(t)
                TimeArr(t) = get24HourClock(TimeArr(t))
                MsgBox(TimeArr(t))
            Catch ex As Exception
                MsgBox(ex)
            End Try

        Next

    End Sub
    Dim TextBox1_record As String
    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        Label1.Text = Format(Now, "yyyy-MM-dd hh:mm:ss")
        Label1.Refresh()
        'Dim NowTime As String = Format(Now, "hh:mm")
        Dim NowTime As String = DateTime.Now.ToString("HH:mm")
        Dim StartTime As String = NowTime
        Dim sec As String = Format(Now, "ss")
        'Dim StartExecOrderArr As Array '= getExecOrder()
        'Dim startProcess As String = ""
        'Dim i As Integer = 0


        'Label5.Text = sec

        'Dim Message, Title, def, MyValue As String
        'Message = "Enter a value between 1 and 3"    ' Set prompt.
        'Title = "InputBox Demo"    ' Set title.
        'def = "1"    ' Set default.
        ' Display message, title, and default value.
        'MyValue = InputBox(Message, Title, def)
        'StartTime = "05:15"
        'MsgBox(StartTime)
        'Dim StartExecOrderArr() As String = {"05:15", "05:20"}
        'StartFlag = True


        '讀取時間到陣列
        'StartExecOrderArr

        If StartFlag Then

            '比對現在時間NowTime
            'For Each StartTime In StartExecOrderArr

            'Next
            'MsgBox(getExecOrder(ExceOrederIndex))
            'MsgBox(get24HourClock(getExecOrder(0)))
            'If String.Compare(StartTime, StartExecOrderArr(ExceOrederIndex)) = 0 Then '若執行後ExceOrderIndex加1等待執行下一個
            'MsgBox("456")

            'MsgBox(ExceOrederIndex)

            'MsgBox(StartTime)
            'MsgBox(get24HourClock(getExecOrder(ExceOrederIndex)))
            If sec = 0 Then
                ExceOrederIndex = 0
                'MsgBox("123 " & ExceOrederIndex)
            End If
            'Label5.Text = ExceOrederIndex
            'Label5.Refresh()
            'MsgBox(ExceOrederIndex)
            'MsgBox(StartTime & "vs" & get24HourClock(getExecOrder(ExceOrederIndex)))
            'MsgBox(String.Compare(StartTime, get24HourClock(getExecOrder(ExceOrederIndex))) = 0)

            If String.Compare(StartTime, get24HourClock(getExecOrder(ExceOrederIndex))) = 0 Then
                Dim p As String
                p = getExecProcess(ExceOrederIndex)
                'If String.Compare(StartTime, get24HourClock(getExecOrder(ExceOrederIndex))) = 0 Then
                'If StartTime = StartExecOrderArr(ExceOrederIndex) Then 
                'MsgBox("123")
                'MsgBox(ExceOrederIndex & ":" & StartExecOrderArr(ExceOrederIndex))
                '取得路徑
                Dim StartProcess As Cmd = New Cmd()
                'MsgBox(get24HourClock(getExecOrder(ExceOrederIndex)))
                'MsgBox("時間到")
                'MsgBox(getExecProcess(ExceOrederIndex))
                'Label5.Text = "時間到"
                'Label6.Text = getExecProcess(ExceOrederIndex)
                Try
                    'MsgBox("0")
                    'MsgBox("時間到")
                    'MsgBox(getExecProcess(ExceOrederIndex))
                    'Dim file_name As String = CStr(Path.GetFileName(getExecProcess(ExceOrederIndex))) '取得檔名
                    'MsgBox("0.1")
                    'Dim file_path As String = CStr(Path.GetDirectoryName(getExecProcess(ExceOrederIndex))) '取得路徑
                    'MsgBox("1")
                    'Label5.Text = file_name
                    'Label6.Text = file_path
                    'MsgBox("2")
                    StartProcess.cmd("cd " & CStr(Path.GetDirectoryName(p)))
                    'MsgBox(p)
                    StartProcess.cmd(CStr(Path.GetFileName(p)))
                    'MsgBox(CStr(Path.GetFileName(p)))
                    'MsgBox("3")
                Catch ex As System.ArgumentException
                    MsgBox(ex)
                End Try

                'MsgBox(file_path)
                'MsgBox(file_name)
            ElseIf String.Compare(StartTime, get24HourClock(getExecOrder(ExceOrederIndex))) <> 0 Then
                ExceOrederIndex += 1

                'End If
            End If

            'If startOrder Then

            'For Each startOrder In startExecOrderArr
            ' startProcess(i) = getExecProcess(i)
            ' i = i + 1
            ' Next

        End If

    End Sub

    Public Function ArrayLen(arr As Array) As Integer
        ArrayLen = UBound(arr) - LBound(arr) + 1
    End Function

    Sub test()
        'MsgBox(get24HourClock("上午 - 12:00"))
        'MsgBox(get24HourClock("下午 - 11:59"))
        'MsgBox(get24HourClock(getExecOrder(0)))
        'MsgBox(getExecProcess(0))
        'MsgBox(getExecOrder(1))
        'MsgBox(Path.GetFileName("C:\Users\udev77\Desktop\testStart.bat"))
        'MsgBox(Path.GetDirectoryName("C:\Users\udev77\Desktop\testStart.bat"))
    End Sub

    Function getOrderCt() As String 'index As Integer
        Dim fileReader As String
        Dim not_EOL_str As Array = Nothing
        Dim strArray As Array = Nothing
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), System.Text.Encoding.UTF8)
        Dim j As Integer = 0
        Dim k As Integer = 0
        Try
            not_EOL_str = Split(fileReader, vbCrLf)
            getOrderCt = ArrayLen(not_EOL_str) - 1

        Catch ex As Exception
            MsgBox("325")
        End Try



    End Function

    Function getExecOrder(ExecOrderIndex As Integer) As String 'index As Integer
        Dim fileReader As String
        Dim not_EOL_str As Array = Nothing
        Dim strArray As Array = Nothing
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), System.Text.Encoding.UTF8)
        Dim j As Integer = 0
        Dim k As Integer = 0
        Try
            not_EOL_str = Split(fileReader, vbCrLf)
            If String.IsNullOrEmpty(not_EOL_str(ExecOrderIndex)) = False Then
                Try
                    'MsgBox(not_EOL_str(ExecOrderIndex))
                    strArray = Split(not_EOL_str(ExecOrderIndex), ",")
                    'MsgBox(strArray(1))
                    getExecOrder = strArray(1)
                    'MsgBox("123")
                    Exit Function
                Catch ex As Exception
                    'MsgBox(292)
                    'MsgBox(ex)
                End Try
            End If

        Catch ex As Exception
            MsgBox("325")
        End Try



    End Function

    Function getExecProcess(ExecProcessIndex As Integer) As String
        Dim fileReader As String
        Dim not_EOL_str As Array = Nothing
        Dim strArray As Array = Nothing
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), System.Text.Encoding.UTF8)
        Dim j As Integer = 0
        Dim k As Integer = 0
        not_EOL_str = Split(fileReader, vbCrLf)
        'While j < 10
        'DataGridView1.AllowUserToAddRows = False '刪除預設空白列
        For k = 0 To not_EOL_str.Length
            strArray = Split(not_EOL_str(k), ",")
            'MsgBox(strArray(0))
            If k = ExecProcessIndex Then
                If ExecProcessIndex > not_EOL_str.Length - 1 Then
                    Exit For
                End If
                getExecProcess = strArray(0)
                Exit For
            Else
                'getExecProcess = "null"
            End If

            'DataGridView1.Rows.Add(New Object() {strArray(0), strArray(1)})
            '取得啟動時間
        Next
        'getExecProcess = "bbbbbb"
        getExecProcess = ""
    End Function

    Function get24HourClock(timeStr As String) As String
        Dim timeStrArr As Array
        Dim timeArr As Array
        Dim timeArr_Hour As String
        Dim timeArr_Minute As String
        timeStrArr = Split(timeStr, " - ")
        If timeStrArr(0) = "下午" Then
            timeArr = Split(timeStrArr(1), ":")
            timeArr_Hour = CStr(CInt(timeArr(0)) + 12)
            timeArr_Minute = CStr(timeArr(1))
            get24HourClock = timeArr_Hour & ":" & timeArr_Minute
        ElseIf timeStrArr(0) = "上午" Then
            timeArr = Split(timeStrArr(1), ":")
            If String.Compare(timeArr(0), "12") = 0 Then
                timeArr_Hour = CStr(CInt(timeArr(0)) + 12)
            Else
                timeArr_Hour = timeArr(0)
            End If
            timeArr_Minute = CStr(timeArr(1))
            get24HourClock = timeArr_Hour & ":" & timeArr_Minute
        Else
            get24HourClock = "null"
        End If
    End Function

    Function getDataRowCount() As Integer
        getDataRowCount = DataGridView1.Rows.Count
    End Function

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        count += 1
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
        Dim lines As String
        'Shell("cmd.exe")
        Dim cmd_test As Cmd = New Cmd()
        'cmd_test.cmd("cd /d S:\網通部\◎資訊\ & echo eeeee>eeeeeeeeeeeeeee.txt & timeout /t 3 & pause")
        If TextBox1.Text <> TextBox1_record And TextBox1.Text <> "" Then '不一樣則更新
            DataGridView1.Rows.Add(New Object() {TextBox1.Text, ComboBox1.Text})
            '寫入檔案
            lines = TextBox1.Text & "," & ComboBox1.Text
            'Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\ExecOrder.txt"))
            'For Each line As String In lines
            'outputFile.Write(line)
            'Next
            'End Using
            Dim sw As StreamWriter = File.AppendText(mydocpath & Convert.ToString("\ExecOrder.txt"))
            sw.Write(lines & vbCrLf)
            'sw.WriteLine("第二行")
            'sw.WriteLine("第三行")
            sw.Flush()
            sw.Close()
            TextBox1_record = TextBox1.Text
        End If
        If count = 1 And TextBox1.Text <> "" Then
            DataGridView1.AllowUserToAddRows = False '刪除預設空白列
        End If
        DataGridView1.Refresh()


    End Sub
    Private Sub Button2_Click(
    ByVal sender As Object, ByVal e As System.EventArgs) _
    Handles Button2.Click
        Dim selectedCellCount As Integer =
        DataGridView1.GetCellCount(DataGridViewElementStates.Selected)
        If selectedCellCount > 0 Then
            If DataGridView1.AreAllCellsSelected(True) Then
                MessageBox.Show("All cells are selected", "Selected Cells")
            Else
                Dim sb As New System.Text.StringBuilder()
                Dim i As Integer
                Dim now_row As Integer = -1
                Dim now_col As Integer = -1
                Dim WriteStr As String = ""
                For i = 0 To selectedCellCount - 1
                    Dim fileReader As String
                    Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
                    fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), System.Text.Encoding.UTF8)
                    'Dim strArray() As String = strData.Replace("\r", "").Split("\n")
                    Dim strArray() As String = fileReader.Split(vbCrLf)
                    Dim strResult As String = ""
                    Dim sFileText As String = ""
                    Dim replace_str As String = ""
                    Dim replace_str_col As String = ""
                    Dim new_str_col As String = ""
                    now_row = DataGridView1.SelectedCells(i).RowIndex
                    now_col = DataGridView1.SelectedCells(i).ColumnIndex
                    For a = 0 To strArray.Length - 1
                        If a = now_row Then
                            '視窗畫面更新
                            replace_str = DataGridView1.Rows(now_row).Cells(now_col).Value
                            DataGridView1.Rows(now_row).Cells(0).Value = Replace(DataGridView1.Rows(now_row).Cells(0).Value, DataGridView1.Rows(now_row).Cells(0).Value, TextBox1.Text)
                            DataGridView1.Rows(now_row).Cells(1).Value = Replace(DataGridView1.Rows(now_row).Cells(1).Value, DataGridView1.Rows(now_row).Cells(1).Value, ComboBox1.Text)
                            '資料更新
                            If now_col = 0 Then
                                replace_str_col = record_Cell_0 & "," & record_Cell_1
                                new_str_col = Trim(TextBox1.Text & "," & ComboBox1.Text)
                                strArray(now_row) = Replace(strArray(now_row), replace_str_col, new_str_col)
                            ElseIf now_col = 1 Then
                                replace_str_col = record_Cell_0 & "," & record_Cell_1
                                new_str_col = Trim(TextBox1.Text & "," & ComboBox1.Text)
                                strArray(now_row) = Replace(strArray(now_row), replace_str_col, new_str_col)
                            End If
                        End If
                        strArray(a) = Trim(strArray(a)).Replace(vbCrLf, "").Replace(vbLf, "")
                        'WriteStr = WriteStr & strArray(a) & vbCrLf
                        WriteStr &= strArray(a)
                        If a <> strArray.Length - 2 Then
                            WriteStr &= vbCrLf
                        End If
                    Next
                    System.IO.File.WriteAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), WriteStr)
                Next i
            End If
        End If
    End Sub

    Private Sub Button3_Click(
    ByVal sender As Object, ByVal e As System.EventArgs) _
    Handles Button3.Click
        If record_Cell_0 = "" Or record_Cell_1 = "" Then '若未選擇儲存格則不動作
            MsgBox("請選擇刪除資料列")
        Else
            Dim selectedCellCount As Integer =
            DataGridView1.GetCellCount(DataGridViewElementStates.Selected)
            If selectedCellCount > 0 Then
                If DataGridView1.AreAllCellsSelected(True) Then
                    'MessageBox.Show("All cells are selected", "Selected Cells")
                Else
                    Dim sb As New System.Text.StringBuilder()
                    Dim i As Integer
                    Dim now_row As Integer = -1
                    Dim now_col As Integer = -1
                    For i = 0 To selectedCellCount - 1
                        Dim fileReader As String
                        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
                        fileReader = My.Computer.FileSystem.ReadAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), System.Text.Encoding.UTF8)
                        'Dim strArray() As String = fileReader.Replace("\r", "").Split("\n")
                        Dim strArray() As String = fileReader.Split(vbCrLf)
                        Dim strResult As String = ""
                        Dim sFileText As String = ""
                        Dim replace_str As String = ""
                        Dim replace_str_col As String = ""
                        Dim new_str_col As String = ""
                        '視窗畫面更新
                        Dim record_strArray As String
                        now_row = DataGridView1.SelectedCells(i).RowIndex
                        now_col = DataGridView1.SelectedCells(i).ColumnIndex
                        replace_str = DataGridView1.Rows(now_row).Cells(now_col).Value
                        record_strArray = strArray(now_row)
                        DataGridView1.Rows.RemoveAt(DataGridView1.SelectedCells(i).RowIndex) '刪除列
                        '資料更新
                        replace_str_col = record_Cell_0 & "," & record_Cell_1
                        new_str_col = ""

                        For a = 0 To strArray.Length - 1
                            strArray(a) = Replace(strArray(a), replace_str_col, new_str_col) '刪除列
                            If record_strArray <> strArray(a) Then
                                System.IO.File.WriteAllText(mydocpath & Convert.ToString("\ExecOrder.txt"), strArray(a))
                                Exit For
                            End If
                            'MsgBox(strArray(a))

                            'MsgBox(strArray(0))
                            'MsgBox(strArray(1))
                            'MsgBox(strArray(2))
                            'MsgBox(strArray(3))
                            'MsgBox(strArray(4))
                            'MsgBox(strArray.Length)
                            'If strArray.Length > 1 Then
                            'MsgBox(strArray.Length)
                            'MsgBox(DataGridView1.Rows(now_row - 1).Cells(1).Value & vbCrLf)
                            'strArray(a) = Replace(strArray(a), DataGridView1.Rows(now_row - 1).Cells(1).Value & vbCrLf,
                            'DataGridView1.Rows(now_row - 1).Cells(1).Value) '去除換行
                            'End If

                            'MsgBox(strArray(a))
                        Next
                    Next i
                End If
            End If
            '清除已刪除的儲存格的記錄
            record_Cell_0 = ""
            record_Cell_1 = ""
        End If

    End Sub

    Private Sub DataGridView1_CellClick(sender As Object, e As DataGridViewCellEventArgs) Handles DataGridView1.CellClick
        'TextBox1.Text = ""
        Dim selectedCellCount As Integer =
        DataGridView1.GetCellCount(DataGridViewElementStates.Selected)
        If selectedCellCount > 0 Then
            If DataGridView1.AreAllCellsSelected(True) Then
                MessageBox.Show("All cells are selected", "Selected Cells")
            Else
                Dim i As Integer
                'Dim j As Integer
                Dim now_row As Integer
                Dim now_col As Integer

                For i = 0 To selectedCellCount - 1
                    now_row = DataGridView1.SelectedCells(i).RowIndex
                    now_col = DataGridView1.SelectedCells(i).ColumnIndex
                    'For j = 0 To selectedCellCount - 1

                    '若跟之前的列數一樣則不更動
                    If now_row <> record_row Then
                        TextBox1.Text = DataGridView1.Rows(now_row).Cells(0).Value
                        ComboBox1.Text = DataGridView1.Rows(now_row).Cells(1).Value
                    End If
                    record_Cell_0 = DataGridView1.Rows(now_row).Cells(0).Value
                    record_Cell_1 = DataGridView1.Rows(now_row).Cells(1).Value
                    record_row = DataGridView1.SelectedCells(i).RowIndex
                    'Next
                Next
            End If
        End If
        DataGridView1.Refresh()
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        '設定啟動旗標
        If StartFlag = False Then '若未被按下則設為True
            Label4.Text = "啟動自動執行中"
            'Label4.BackColor = Color.Green '背景顏色
            Label4.ForeColor = Color.Green '字體顏色
            Label4.Font = New Font("", 10, FontStyle.Regular) '字體、大小、粗細
            StartFlag = True
        ElseIf StartFlag = True Then '若被按下則設為False
            Label4.Text = "啟動自動尚未執行"
            'Label4.BackColor = Color.Green '背景顏色
            Label4.ForeColor = Color.Red '字體顏色
            Label4.Font = New Font("", 10, FontStyle.Regular) '字體、大小、粗細
            StartFlag = False
        End If

    End Sub
End Class

Public Class Cmd
    Public setpath As String '保存執行路徑的屬性
    Sub cmd(cmd_str As String)
        Dim str_arr() As String
        Dim shell_result As String
        str_arr = Split(cmd_str, " ")
        If String.Compare("cd", str_arr(0)) = 0 Then '是cd指令
            Dim i As Integer
            Dim last_cmd_str As String = ""
            For i = 1 To str_arr.Length - 1 '把cd後面的字串組起來
                last_cmd_str = last_cmd_str & " " & str_arr(i)
            Next
            setpath = last_cmd_str '並儲存
        Else '不是cd指令
            shell_result = shell("cmd.exe", "/k cd " & setpath & " & " & cmd_str)
        End If
    End Sub

    Public Function shell(ByVal command As String, ByVal argument As String) As Integer
        Dim oProcess As New Process()
        Dim oStartInfo As New ProcessStartInfo(command, argument) With {
            .WindowStyle = ProcessWindowStyle.Hidden, '不顯示視窗
            .CreateNoWindow = True, ''不顯示視窗
            .UseShellExecute = False,
            .RedirectStandardOutput = True '不顯示視窗
            }
        oProcess.StartInfo = oStartInfo
        oProcess.Start()
        waitForEnd(oProcess) 'wait
        Return 0
    End Function

    Public Sub waitForEnd(oProcess As Process) 'NOP
        Dim sOutput As String
        Using oStreamReader As System.IO.StreamReader = oProcess.StandardOutput
            sOutput = oStreamReader.ReadToEnd()
        End Using
    End Sub

End Class


Imports MySql.Data.MySqlClient
Imports System
Imports System.IO
Imports MySql.Data
Public Class Form3
    Public sqlconn As New MySqlConnection
    Public KDBconnBackUp As New MySqlConnection
    Public KDBconnLib As New MySqlConnection

    'Dim fileReader As String = My.Computer.FileSystem.ReadAllText("C:\Users\uacc51\Desktop\test.txt")
    'Dim fileReader As String = My.Computer.FileSystem.ReadAllText("C:\Users\udev77\Desktop\test.txt")
    'Dim host As String = fileReader '讀取設定文件
    ReadOnly host As String = "localhost"
    ReadOnly pwd As String = "16264386"
    Private value1 As String
    Private value2 As String
    Private value3 As String
    Private value4 As String
    Private mySqlSysTime As String
    Dim cmd As String
    'Private OpenFileDialog1 As Object
    'Dim str As String





    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Label7.Text = ""
        'Label9.Text = ""
        Label10.Text = DateAndTime.Now '系統時間
        'Label11.Text = CStr(DateTimePicker1.Value)
        'TextBox4.Visible = False
        getData() '讀取資料




    End Sub


    Public Sub GetMySqlConn()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        'Dim tmpSql As String
        If sqlconn.State = ConnectionState.Open Then sqlconn.Close() '若第二次重複連線需關閉
        sqlconn = New MySqlConnection(connString)
        'MsgBox(connString)
        sqlconn.Open()
        If sqlconn Is Nothing Then
            If connString = " " Then
                MsgBox("未設定連線字串", connString)
            Else
                sqlconn = New MySqlConnection(connString)
                sqlconn.Open() '正常連結資料庫
                MsgBox("ok")
            End If
        Else
        End If
        If sqlconn Is Nothing Then MsgBox("MYSQL資料庫連線失敗")
    End Sub
    Public Sub getData()
        Dim da As New MySqlDataAdapter
        Dim ds As New DataSet

        GetMySqlConn()
        Dim str1 As String = "Select UID AS 員工編號,Dept AS 部門,Name AS 人員,Target AS 業績目標 from members;"
        'Dim str1 As String = "Select UID AS 員工編號,Dept AS 部門,Name AS 人員 from members;"
        Dim adp1 As MySqlDataAdapter = New MySqlDataAdapter(str1, sqlconn)

        '將查詢結果放到記憶體set1上的1a表格內
        Dim set1 As DataSet = New DataSet

        adp1.Fill(set1, "1a")

        '將記憶體的資料集合存放到視窗畫面上的DataGrid上
        DataGridView1.DataSource = set1.Tables("1a")

        '關閉資料庫的連結
        sqlconn.Close()

        'Label7.Text = "讀取完畢，共" & DataGridView1.RowCount - 1 & "筆資料。"
        Label7.Text = "讀取完畢，共" & getDataRowCount() & "筆資料。"
        If getDataRowCount() <> DataGridView1.RowCount - 1 Then
            'MsgBox("Data row count error!", "error")
        End If
        getLastUpdatedTime()
        'DataGridView1.Rows.RemoveAt(35)
    End Sub
    Public Sub DataGridView1_CellClick(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles DataGridView1.CellClick
        'get the selected row in datagridview
        Dim i As Integer
        i = DataGridView1.CurrentRow.Index
        '等同DataGridView1.BindingContext(DataGridView1.DataSource).Position + 1
        If i = getDataRowCount() Then Exit Sub
        Try
            TextBox1.Text = DataGridView1.Item(0, i).Value
            TextBox2.Text = DataGridView1.Item(1, i).Value
            TextBox3.Text = DataGridView1.Item(2, i).Value
            TextBox4.Text = DataGridView1.Item(3, i).Value
        Catch ex As Exception
            'MsgBox("無資料")
        End Try
        'DataGridView1.FirstDisplayedScrollingRowIndex = i - 3
        'posX = DataGridView1.BindingContext(DataGridView1.DataSource).Position
        'MsgBox(posX)

        'DataGridView1唯讀
        DataGridView1.Columns("員工編號").ReadOnly = True
        DataGridView1.Columns("部門").ReadOnly = True
        DataGridView1.Columns("人員").ReadOnly = True
        DataGridView1.Columns("業績目標").ReadOnly = True
    End Sub

    Public Function getMySqlSysTime()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        Dim sqlconn As MySqlConnection = New MySqlConnection(connString)

        cmd = "select concat(CURRENT_DATE," & Chr(34) & " " & Chr(34) & ",CURRENT_TIME) AS SysTime;"
        'MsgBox(cmd)
        Dim myCommand As MySqlCommand = New MySqlCommand(cmd, sqlconn)
        sqlconn.Open()
        Dim myReader As MySqlDataReader
        myReader = myCommand.ExecuteReader()

        Try
            While (myReader.Read)
                mySqlSysTime = myReader.GetString(0)
            End While
            sqlconn.Close()
        Catch ex As Exception
            MsgBox("Error occured: Could not D_modified record", "Error 01")
        End Try
        Return mySqlSysTime

    End Function
    Public Function getDataRowCount()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        Dim sqlconn As MySqlConnection = New MySqlConnection(connString)
        cmd = "select count(*) from membersDB.members;"
        'cmd = "select count(*) from members;"
        'MsgBox(cmd)
        'MsgBox(sqlconn)
        Dim myCommand As MySqlCommand = New MySqlCommand(cmd, sqlconn)
        sqlconn.Open()
        Dim myReader As MySqlDataReader
        myReader = myCommand.ExecuteReader()
        Dim dataRowCount As Integer
        Try
            While (myReader.Read)
                dataRowCount = myReader.GetString(0)
            End While
            sqlconn.Close()
        Catch ex As Exception
            MsgBox("Error occured: Could not D_modified record", "Error 02")
        End Try
        Return dataRowCount

    End Function
    Public Sub getLastUpdatedTime()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        Dim sqlconn As MySqlConnection = New MySqlConnection(connString)

        'cmd = "select max(D_modified) from members;"
        '只取D_modified最大值
        'cmd = "select max(num) from (select D_created as num from members UNION select D_modified as num from members) AS tblNums;"
        '取 D_created & D_modified最大值 但沒as 程式會錯 SQL對
        'cmd = "select max(num) as maxnum from (select D_created as num from members UNION select D_modified as num from members) AS tblNums;"
        'MsgBox(cmd)
        Dim myCommand As MySqlCommand = New MySqlCommand(cmd, sqlconn)
        sqlconn.Open()
        Dim myReader As MySqlDataReader
        myReader = myCommand.ExecuteReader()
        'MsgBox(myReader.GetString(0))
        Try
            While (myReader.Read)
                'Label9.Text = myReader.GetString(0)
            End While
            sqlconn.Close()
        Catch ex As Exception
            MsgBox("Error occured: Could not D_modified record", "Error 03")
        End Try

    End Sub

    Public Sub recordDateCreated()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        If sqlconn.State = ConnectionState.Open Then sqlconn.Close() '若第二次重複連線需關閉
        sqlconn = New MySqlConnection(connString)
        sqlconn.Open()
        Try
            cmd = "Update members set D_created=concat(curdate()," & Chr(34) & " " & Chr(34) & ",curtime()) where UID = " & TextBox1.Text & ";"
            'MsgBox(cmd)
            Dim cn As New MySqlCommand(cmd, sqlconn)
            cn.ExecuteNonQuery()

            sqlconn.Close()
        Catch ex As Exception
            MsgBox("Error occured: Could not insert record", "Error 04")
        End Try
    End Sub
    Public Sub recordDateModified()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        If sqlconn.State = ConnectionState.Open Then sqlconn.Close() '若第二次重複連線需關閉
        sqlconn = New MySqlConnection(connString)
        sqlconn.Open()
        Try
            cmd = "Update members set D_modified=concat(curdate()," & Chr(34) & " " & Chr(34) & ",curtime()) where UID = " & TextBox1.Text & ";"
            'MsgBox(cmd)

            Dim cn As New MySqlCommand(cmd, sqlconn)
            cn.ExecuteNonQuery()

            sqlconn.Close()
        Catch ex As Exception
            MsgBox("Error occured: Could not insert record", "Error 05")
        End Try
    End Sub

    Public Sub insertData()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        If sqlconn.State = ConnectionState.Open Then sqlconn.Close() '若第二次重複連線需關閉
        sqlconn = New MySqlConnection(connString)
        sqlconn.Open()
        Try
            If value4 = "" Then '業績目標若為空,自動填0
                value4 = 0
            End If
            cmd = "INSERT INTO members (UID,Dept, name, target)
        VALUES(" & Chr(34) & value1 & Chr(34) & "," & Chr(34) & value2 & Chr(34) &
        "," & Chr(34) & value3 & Chr(34) & "," & Chr(34) & value4 & Chr(34) & ");"
            'INSERT INTO "表格名" ("欄位1", "欄位2", ...)
            'VALUES("值1", "值2", ...);
            Dim cn As New MySqlCommand(cmd, sqlconn)
            cn.ExecuteNonQuery()
            recordDateCreated() '記錄新增時間
            sqlconn.Close()
            Label7.Text = "已新增資料!"
        Catch ex As Exception '若輸入相同UID會執行這段，因為UID在SQL設定為key，重覆會產生錯誤。
            MsgBox("新增資料失敗，編號重覆", 0, "訊息")
            'MsgBox("Error occured: Could not insert record", "Error 06")'避免還要TextBox4字串轉成數字被判定無效
        End Try
        getData()

    End Sub

    Public Sub updateData()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        If sqlconn.State = ConnectionState.Open Then sqlconn.Close() '若第二次重複連線需關閉
        sqlconn = New MySqlConnection(connString)
        sqlconn.Open()
        Try
            If value4 = "" Then '業績目標若為空,自動填0
                value4 = 0
            End If
            cmd = "UPDATE members
        SET Dept = " & Chr(34) & value2 & Chr(34) & ", Name = " & Chr(34) & value3 & Chr(34) & ", Target = " & Chr(34) & value4 &
Chr(34) & " WHERE UID = " & TextBox1.Text & ";"
            'MsgBox(cmd)
            'UPDATE "表格"
            'SET "欄位1" = [值1], "欄位2" = [值2]
            'WHERE "條件";
            'MsgBox(cmd)
            Dim cn As New MySqlCommand(cmd, sqlconn)
            cn.ExecuteNonQuery()
            recordDateModified() '記錄修改時間
            sqlconn.Close()
        Catch ex As Exception
            MsgBox("Error occured: Could not insert record")
        End Try
        getData()
    End Sub

    Public Sub deleteData()
        Dim connString As String = "Database=membersDB;Data Source=" & host & ";User Id=root;Password=" & pwd & ";CharSet=utf8"
        If sqlconn.State = ConnectionState.Open Then sqlconn.Close() '若第二次重複連線需關閉
        sqlconn = New MySqlConnection(connString)
        sqlconn.Open()
        Try
            If value1 <> "" Then
                cmd = "DELETE FROM members
        WHERE UID = " & value1 & ";"
                'DELETE FROM "表格名"
                'WHERE "條件";
                Dim cn As New MySqlCommand(cmd, sqlconn)
                cn.ExecuteNonQuery()
                sqlconn.Close()
            End If
        Catch ex As Exception
            MsgBox("Error occured: Could not insert record", "Error 08")
        End Try
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        '檢視已儲存資料按鈕
        getData()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        '新增資料按鈕
        Dim posX As Integer
        posX = DataGridView1.CurrentRow.Index
        'If DataGridView1.CurrentRow.Index <> Nothing Then '取得目前所選資料列不為空
        If getFoolProof() = False Then '防呆
            Exit Sub
        End If
        insertData() '新增
        clearTextBox() '清空
        getData()
        'DataGridView1.FirstDisplayedScrollingColumnIndex = posX
        getLastUpdatedTime() '顯示最後更新時間 資料更新時間
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        '修改資料按鈕
        Dim posX As Integer
        posX = DataGridView1.CurrentRow.Index
        If getFoolProof() = False Then '防呆
            Exit Sub
        End If
        updateData()
        clearTextBox() '清空
        getData()
        DataGridView1.FirstDisplayedScrollingRowIndex = posX
        Label7.Text = "已修改資料!"
        getLastUpdatedTime() '顯示最後更新時間 資料更新時間
    End Sub
    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        '刪除資料按鈕
        Dim msgstr As String
        Dim result As Long
        msgstr = "確定要刪除選取資料列?" & vbCrLf & TextBox1.Text & "," & TextBox2.Text & "," & TextBox3.Text & "," & TextBox4.Text
        result = MsgBox(msgstr, vbYesNo, "確認刪除提示")
        Select Case result
            Case vbYes
                Dim posX As Integer
                posX = DataGridView1.CurrentRow.Index
                'If getFoolProof() = False Then '防呆
                'Exit Sub
                'End If
                deleteData()
                clearTextBox()
                getData()
                DataGridView1.FirstDisplayedScrollingRowIndex = posX
                'Label9.Text = getMySqlSysTime() '顯示最後更新時間 系統時間
                Label7.Text = "已刪除資料!"
            Case vbNo

        End Select

    End Sub
    Public Function textbox1_textchanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged
        value1 = TextBox1.Text
        Return value1
    End Function
    Private Function TextBox2_TextChanged(sender As Object, e As EventArgs) Handles TextBox2.TextChanged
        value2 = TextBox2.Text
        Return value2
    End Function
    Private Function TextBox3_TextChanged(sender As Object, e As EventArgs) Handles TextBox3.TextChanged
        value3 = TextBox3.Text
        Return value3
    End Function
    Private Function TextBox4_TextChanged(sender As Object, e As EventArgs) Handles TextBox4.TextChanged
        value4 = TextBox4.Text
        Return value4
    End Function

    Function isAlphaOrDigit(str As String) As Boolean
        '判斷是否為英數

        Dim r As String = StrConv(str, VbStrConv.Narrow)
        Dim b As Boolean = False
        For i As Integer = 0 To r.Length - 1
            Dim t As Integer = Asc(r.ToUpper.Substring(i, 1))
            '第48~57號為0~9十個阿拉伯數字；
            '65~90號為26個大寫英文字母，
            '97~122號為26個小寫英文字母
            If ((t >= 97 And t <= 122) Or (t >= 65 And t <= 90) Or (t >= 48 And t <= 57)) Then
                b = True
                Exit For
            End If
        Next
        Return b
    End Function
    Function isDigit(str As String) As Boolean
        '判斷是否為數字

        Dim r As String = StrConv(str, VbStrConv.Narrow)
        Dim b As Boolean = False
        For i As Integer = 0 To r.Length - 1
            Dim t As Integer = Asc(r.ToUpper.Substring(i, 1))
            '第48~57號為0~9十個阿拉伯數字；
            '65~90號為26個大寫英文字母，
            '97~122號為26個小寫英文字母
            If (t >= 48 And t <= 57) Then
                b = True
                Exit For
            End If
        Next
        Return b
    End Function



    'Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs)

    'Dim today As Date
    'Dim answer As String
    'today = Convert.ToDateTime(System.DateTime.Now.Year.ToString() & "/" & "選擇月份" + 1 & "/" & "1")
    'answer = today.AddDays(-1).Day.ToString()
    'ComboBox1.Text = answer

    'End Sub

    Private Sub 離開ToolStripMenuItem_Click(sender As Object, e As EventArgs)
        If MessageBox.Show("確定要離開系統嗎?", "", MessageBoxButtons.YesNo) = Windows.Forms.DialogResult.Yes Then
            Application.Exit()
        Else
        End If
    End Sub
    Private Sub dataGridView1_Sorted(ByVal sender As Object,
    ByVal e As System.EventArgs) Handles DataGridView1.Sorted

        Me.DataGridView1.FirstDisplayedCell = Me.DataGridView1.CurrentCell

    End Sub

    Private Sub 設定ToolStripMenuItem_Click(sender As Object, e As EventArgs)
        'MessageBox.Show("請輸入資料庫主機IP")
        'XtraInputBox.Show("Enter a new value", "Change Settings", "Default")
        'Application.InputBox("Enter your salesID:", "Input Box Text", Type:=1)
        Dim lines As String
        lines = InputBox("請輸入資料庫主機IP", "IP設定", "請輸入資料庫主機IP")
        ' Create a string array with the lines of text
        'Dim lines() As String = {"First line", "Second line", "Third line"}

        ' Set a variable to the My Documents path.
        Dim mydocpath As String = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)

        ' Write the string array to a new file named "WriteLines.txt".
        Using outputFile As New StreamWriter(mydocpath & Convert.ToString("\WriteLines.txt"))
            For Each line As String In lines
                outputFile.WriteLine(line)
            Next
            MsgBox(mydocpath & Convert.ToString("\WriteLines.txt"))
        End Using
        'C:\Program Files\
    End Sub

    Private Sub DataGridView1_CellContentClick(sender As Object, e As DataGridViewCellEventArgs) Handles DataGridView1.CellContentClick

    End Sub

    Public Function maxDate(y As Integer, m As Integer)


        If m Mod 2 = 0 And m <> 2 And m <= 7 Or m Mod 2 = 1 And m > 7 Then
            Return 30
        End If
        If m Mod 2 = 1 And m <= 7 Or m Mod 2 = 0 And m > 7 Then
            Return 31
        End If
        If m = 2 Then
            If y Mod 4 = 0 And y Mod 100 <> 0 Or y Mod 400 = 0 Then
                Return 29
            Else
                Return 28
            End If
        End If
        '以上都是在判斷該月份是幾天
        Return -1

    End Function

    Public Function getFoolProof() As Boolean
        '防呆

        Label5.Text = ""
        '判斷TextBox1~3 任一字串為空皆跳出
        If TextBox1.Text Is String.Empty Or TextBox2.Text Is String.Empty Or TextBox3.Text Is String.Empty Then
            Label5.ForeColor = Color.Red
            Label5.Text = "員工編號、部門、人員需填。"
            Return False
        End If
        '判斷TextBox1內容  不是英文數字
        If isAlphaOrDigit(TextBox1.Text) = False Then
            Label5.ForeColor = Color.Red
            Label5.Text = "員工編號必須英文或數字。"
            Return False
        End If
        '判斷TextBox4內容  不是數字
        If isDigit(TextBox4.Text) = False Then
            Label5.ForeColor = Color.Red
            'Label5.Text = "業績目標需填數字，若沒填則系統將自動填0。"
            '此處不需Return False 因為已自動填0了
        End If
        Return True
    End Function
    Public Sub clearTextBox()
        TextBox1.Text = ""
        TextBox2.Text = ""
        TextBox3.Text = ""
        TextBox4.Text = ""
    End Sub

End Class


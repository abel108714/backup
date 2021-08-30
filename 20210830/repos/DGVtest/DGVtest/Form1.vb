Public Class Form1
	Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
		'For i As Integer = 1 To 9
		'	ComboBox1.Items.Add(i)
		'	Next

		'DataGridView1.Columns.Add("datetime", "日期時間")
		'DataGridView1.Columns.Add("name", "姓名")
		'DataGridView1.Columns.Add("music", "播放音樂")
		'DataGridView1.Columns.Add("col", "期望效果")
		'
		DataGridView1.Rows.Add(New Object() {"2008/6/1 17:05:08", "早日康復", "", ""})
		DataGridView1.Rows.Add(New Object() {"2008/6/1 17:05:09", "王小美", "", ""})

		'DataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect
	End Sub

	Private Sub ComboBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles ComboBox1.SelectedIndexChanged
		'Dim dgr As DataGridViewRow

		'For Each dgr In Me.DataGridView1.Rows
		'	dgr.Cells("music").Value = ComboBox1.SelectedItem.ToString()
		'		Next
	End Sub
End Class

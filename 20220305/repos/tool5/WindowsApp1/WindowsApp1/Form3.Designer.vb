<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form3
	Inherits System.Windows.Forms.Form

	'Form 覆寫 Dispose 以清除元件清單。
	<System.Diagnostics.DebuggerNonUserCode()>
	Protected Overrides Sub Dispose(ByVal disposing As Boolean)
		Try
			If disposing AndAlso components IsNot Nothing Then
				components.Dispose()
			End If
		Finally
			MyBase.Dispose(disposing)
		End Try
	End Sub

	'為 Windows Form 設計工具的必要項
	Private components As System.ComponentModel.IContainer

	'注意: 以下為 Windows Form 設計工具所需的程序
	'可以使用 Windows Form 設計工具進行修改。
	'請勿使用程式碼編輯器進行修改。
	<System.Diagnostics.DebuggerStepThrough()>
	Private Sub InitializeComponent()
		Me.Label1 = New System.Windows.Forms.Label()
		Me.Label2 = New System.Windows.Forms.Label()
		Me.Label3 = New System.Windows.Forms.Label()
		Me.Label4 = New System.Windows.Forms.Label()
		Me.Label5 = New System.Windows.Forms.Label()
		Me.Label7 = New System.Windows.Forms.Label()
		Me.Label10 = New System.Windows.Forms.Label()
		Me.DataGridView1 = New System.Windows.Forms.DataGridView()
		Me.Button1 = New System.Windows.Forms.Button()
		Me.Button2 = New System.Windows.Forms.Button()
		Me.Button3 = New System.Windows.Forms.Button()
		Me.Button4 = New System.Windows.Forms.Button()
		Me.TextBox1 = New System.Windows.Forms.TextBox()
		Me.TextBox2 = New System.Windows.Forms.TextBox()
		Me.TextBox3 = New System.Windows.Forms.TextBox()
		Me.TextBox4 = New System.Windows.Forms.TextBox()
		CType(Me.DataGridView1, System.ComponentModel.ISupportInitialize).BeginInit()
		Me.SuspendLayout()
		'
		'Label1
		'
		Me.Label1.AutoSize = True
		Me.Label1.Location = New System.Drawing.Point(67, 67)
		Me.Label1.Name = "Label1"
		Me.Label1.Size = New System.Drawing.Size(53, 12)
		Me.Label1.TabIndex = 0
		Me.Label1.Text = "員工編號"
		'
		'Label2
		'
		Me.Label2.AutoSize = True
		Me.Label2.Location = New System.Drawing.Point(91, 95)
		Me.Label2.Name = "Label2"
		Me.Label2.Size = New System.Drawing.Size(29, 12)
		Me.Label2.TabIndex = 1
		Me.Label2.Text = "部門"
		'
		'Label3
		'
		Me.Label3.AutoSize = True
		Me.Label3.Location = New System.Drawing.Point(91, 123)
		Me.Label3.Name = "Label3"
		Me.Label3.Size = New System.Drawing.Size(29, 12)
		Me.Label3.TabIndex = 2
		Me.Label3.Text = "人員"
		'
		'Label4
		'
		Me.Label4.AutoSize = True
		Me.Label4.Location = New System.Drawing.Point(67, 151)
		Me.Label4.Name = "Label4"
		Me.Label4.Size = New System.Drawing.Size(53, 12)
		Me.Label4.TabIndex = 3
		Me.Label4.Text = "業績目標"
		'
		'Label5
		'
		Me.Label5.AutoSize = True
		Me.Label5.Location = New System.Drawing.Point(68, 235)
		Me.Label5.Name = "Label5"
		Me.Label5.Size = New System.Drawing.Size(0, 12)
		Me.Label5.TabIndex = 4
		'
		'Label7
		'
		Me.Label7.AutoSize = True
		Me.Label7.Location = New System.Drawing.Point(68, 504)
		Me.Label7.Name = "Label7"
		Me.Label7.Size = New System.Drawing.Size(37, 12)
		Me.Label7.TabIndex = 6
		Me.Label7.Text = "Label7"
		'
		'Label10
		'
		Me.Label10.AutoSize = True
		Me.Label10.Location = New System.Drawing.Point(278, 37)
		Me.Label10.Name = "Label10"
		Me.Label10.Size = New System.Drawing.Size(43, 12)
		Me.Label10.TabIndex = 9
		Me.Label10.Text = "Label10"
		'
		'DataGridView1
		'
		Me.DataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		Me.DataGridView1.Location = New System.Drawing.Point(70, 260)
		Me.DataGridView1.Name = "DataGridView1"
		Me.DataGridView1.RowTemplate.Height = 24
		Me.DataGridView1.Size = New System.Drawing.Size(479, 218)
		Me.DataGridView1.TabIndex = 10
		'
		'Button1
		'
		Me.Button1.Location = New System.Drawing.Point(70, 193)
		Me.Button1.Name = "Button1"
		Me.Button1.Size = New System.Drawing.Size(75, 23)
		Me.Button1.TabIndex = 11
		Me.Button1.Text = "檢視"
		Me.Button1.UseVisualStyleBackColor = True
		'
		'Button2
		'
		Me.Button2.Location = New System.Drawing.Point(164, 193)
		Me.Button2.Name = "Button2"
		Me.Button2.Size = New System.Drawing.Size(75, 23)
		Me.Button2.TabIndex = 12
		Me.Button2.Text = "新增"
		Me.Button2.UseVisualStyleBackColor = True
		'
		'Button3
		'
		Me.Button3.Location = New System.Drawing.Point(258, 193)
		Me.Button3.Name = "Button3"
		Me.Button3.Size = New System.Drawing.Size(75, 23)
		Me.Button3.TabIndex = 13
		Me.Button3.Text = "修改"
		Me.Button3.UseVisualStyleBackColor = True
		'
		'Button4
		'
		Me.Button4.Location = New System.Drawing.Point(351, 193)
		Me.Button4.Name = "Button4"
		Me.Button4.Size = New System.Drawing.Size(75, 23)
		Me.Button4.TabIndex = 14
		Me.Button4.Text = "刪除"
		Me.Button4.UseVisualStyleBackColor = True
		'
		'TextBox1
		'
		Me.TextBox1.Location = New System.Drawing.Point(129, 64)
		Me.TextBox1.Name = "TextBox1"
		Me.TextBox1.Size = New System.Drawing.Size(100, 22)
		Me.TextBox1.TabIndex = 15
		'
		'TextBox2
		'
		Me.TextBox2.Location = New System.Drawing.Point(129, 92)
		Me.TextBox2.Name = "TextBox2"
		Me.TextBox2.Size = New System.Drawing.Size(100, 22)
		Me.TextBox2.TabIndex = 16
		'
		'TextBox3
		'
		Me.TextBox3.Location = New System.Drawing.Point(129, 120)
		Me.TextBox3.Name = "TextBox3"
		Me.TextBox3.Size = New System.Drawing.Size(100, 22)
		Me.TextBox3.TabIndex = 17
		'
		'TextBox4
		'
		Me.TextBox4.Location = New System.Drawing.Point(129, 148)
		Me.TextBox4.Name = "TextBox4"
		Me.TextBox4.Size = New System.Drawing.Size(100, 22)
		Me.TextBox4.TabIndex = 18
		'
		'Form3
		'
		Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 12.0!)
		Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		Me.ClientSize = New System.Drawing.Size(623, 549)
		Me.Controls.Add(Me.TextBox4)
		Me.Controls.Add(Me.TextBox3)
		Me.Controls.Add(Me.TextBox2)
		Me.Controls.Add(Me.TextBox1)
		Me.Controls.Add(Me.Button4)
		Me.Controls.Add(Me.Button3)
		Me.Controls.Add(Me.Button2)
		Me.Controls.Add(Me.Button1)
		Me.Controls.Add(Me.DataGridView1)
		Me.Controls.Add(Me.Label10)
		Me.Controls.Add(Me.Label7)
		Me.Controls.Add(Me.Label5)
		Me.Controls.Add(Me.Label4)
		Me.Controls.Add(Me.Label3)
		Me.Controls.Add(Me.Label2)
		Me.Controls.Add(Me.Label1)
		Me.Name = "Form3"
		Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		Me.Text = "部門人員資料設定"
		CType(Me.DataGridView1, System.ComponentModel.ISupportInitialize).EndInit()
		Me.ResumeLayout(False)
		Me.PerformLayout()

	End Sub

	Friend WithEvents Label1 As Label
	Friend WithEvents Label2 As Label
	Friend WithEvents Label3 As Label
	Friend WithEvents Label4 As Label
	Friend WithEvents Label5 As Label
	Friend WithEvents Label7 As Label
	Friend WithEvents Label10 As Label
	Friend WithEvents DataGridView1 As DataGridView
	Friend WithEvents Button1 As Button
	Friend WithEvents Button2 As Button
	Friend WithEvents Button3 As Button
	Friend WithEvents Button4 As Button
	Friend WithEvents TextBox1 As TextBox
	Friend WithEvents TextBox2 As TextBox
	Friend WithEvents TextBox3 As TextBox
	Friend WithEvents TextBox4 As TextBox
End Class

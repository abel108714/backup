<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
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
		Me.components = New System.ComponentModel.Container()
		Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
		Me.Button1 = New System.Windows.Forms.Button()
		Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
		Me.設定ToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.路徑設定ToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.資料設定ToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.開啟檔案自動結束視窗ToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.不顯示小工具介面ToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.離開ToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.Label1 = New System.Windows.Forms.Label()
		Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
		Me.NotifyIcon1 = New System.Windows.Forms.NotifyIcon(Me.components)
		Me.ContextMenuStrip1 = New System.Windows.Forms.ContextMenuStrip(Me.components)
		Me.OpenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.ExitToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
		Me.Label2 = New System.Windows.Forms.Label()
		Me.Button2 = New System.Windows.Forms.Button()
		Me.MenuStrip1.SuspendLayout()
		Me.ContextMenuStrip1.SuspendLayout()
		Me.SuspendLayout()
		'
		'Button1
		'
		Me.Button1.Location = New System.Drawing.Point(120, 116)
		Me.Button1.Name = "Button1"
		Me.Button1.Size = New System.Drawing.Size(141, 55)
		Me.Button1.TabIndex = 0
		Me.Button1.Text = "開啟開發部門業績表"
		Me.Button1.UseVisualStyleBackColor = True
		'
		'MenuStrip1
		'
		Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.設定ToolStripMenuItem})
		Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
		Me.MenuStrip1.Name = "MenuStrip1"
		Me.MenuStrip1.Size = New System.Drawing.Size(381, 24)
		Me.MenuStrip1.TabIndex = 1
		Me.MenuStrip1.Text = "MenuStrip1"
		'
		'設定ToolStripMenuItem
		'
		Me.設定ToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.路徑設定ToolStripMenuItem, Me.資料設定ToolStripMenuItem, Me.開啟檔案自動結束視窗ToolStripMenuItem, Me.不顯示小工具介面ToolStripMenuItem, Me.離開ToolStripMenuItem})
		Me.設定ToolStripMenuItem.Name = "設定ToolStripMenuItem"
		Me.設定ToolStripMenuItem.Size = New System.Drawing.Size(44, 20)
		Me.設定ToolStripMenuItem.Text = "設定"
		'
		'路徑設定ToolStripMenuItem
		'
		Me.路徑設定ToolStripMenuItem.Name = "路徑設定ToolStripMenuItem"
		Me.路徑設定ToolStripMenuItem.Size = New System.Drawing.Size(184, 22)
		Me.路徑設定ToolStripMenuItem.Text = "路徑設定"
		'
		'資料設定ToolStripMenuItem
		'
		Me.資料設定ToolStripMenuItem.Name = "資料設定ToolStripMenuItem"
		Me.資料設定ToolStripMenuItem.Size = New System.Drawing.Size(184, 22)
		Me.資料設定ToolStripMenuItem.Text = "部門人員資料設定"
		'
		'開啟檔案自動結束視窗ToolStripMenuItem
		'
		Me.開啟檔案自動結束視窗ToolStripMenuItem.Name = "開啟檔案自動結束視窗ToolStripMenuItem"
		Me.開啟檔案自動結束視窗ToolStripMenuItem.Size = New System.Drawing.Size(184, 22)
		Me.開啟檔案自動結束視窗ToolStripMenuItem.Text = "開啟檔案後自動結束"
		'
		'不顯示小工具介面ToolStripMenuItem
		'
		Me.不顯示小工具介面ToolStripMenuItem.Name = "不顯示小工具介面ToolStripMenuItem"
		Me.不顯示小工具介面ToolStripMenuItem.Size = New System.Drawing.Size(184, 22)
		Me.不顯示小工具介面ToolStripMenuItem.Text = "不顯示小工具介面"
		'
		'離開ToolStripMenuItem
		'
		Me.離開ToolStripMenuItem.Name = "離開ToolStripMenuItem"
		Me.離開ToolStripMenuItem.Size = New System.Drawing.Size(184, 22)
		Me.離開ToolStripMenuItem.Text = "離開"
		'
		'Label1
		'
		Me.Label1.AutoSize = True
		Me.Label1.Location = New System.Drawing.Point(241, 9)
		Me.Label1.Name = "Label1"
		Me.Label1.Size = New System.Drawing.Size(0, 12)
		Me.Label1.TabIndex = 2
		'
		'OpenFileDialog1
		'
		Me.OpenFileDialog1.FileName = "OpenFileDialog1"
		'
		'NotifyIcon1
		'
		Me.NotifyIcon1.ContextMenuStrip = Me.ContextMenuStrip1
		Me.NotifyIcon1.Icon = CType(resources.GetObject("NotifyIcon1.Icon"), System.Drawing.Icon)
		Me.NotifyIcon1.Text = "NotifyIcon1"
		Me.NotifyIcon1.Visible = True
		'
		'ContextMenuStrip1
		'
		Me.ContextMenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.OpenToolStripMenuItem, Me.ExitToolStripMenuItem})
		Me.ContextMenuStrip1.Name = "ContextMenuStrip1"
		Me.ContextMenuStrip1.Size = New System.Drawing.Size(161, 48)
		'
		'OpenToolStripMenuItem
		'
		Me.OpenToolStripMenuItem.Name = "OpenToolStripMenuItem"
		Me.OpenToolStripMenuItem.Size = New System.Drawing.Size(160, 22)
		Me.OpenToolStripMenuItem.Text = "開啟小工具介面"
		'
		'ExitToolStripMenuItem
		'
		Me.ExitToolStripMenuItem.Name = "ExitToolStripMenuItem"
		Me.ExitToolStripMenuItem.Size = New System.Drawing.Size(160, 22)
		Me.ExitToolStripMenuItem.Text = "離開"
		'
		'Label2
		'
		Me.Label2.AutoSize = True
		Me.Label2.Location = New System.Drawing.Point(332, 336)
		Me.Label2.Name = "Label2"
		Me.Label2.Size = New System.Drawing.Size(37, 12)
		Me.Label2.TabIndex = 3
		Me.Label2.Text = "Label2"
		'
		'Button2
		'
		Me.Button2.Location = New System.Drawing.Point(120, 227)
		Me.Button2.Name = "Button2"
		Me.Button2.Size = New System.Drawing.Size(141, 55)
		Me.Button2.TabIndex = 4
		Me.Button2.Text = "開啟網通部門業績表"
		Me.Button2.UseVisualStyleBackColor = True
		'
		'Form1
		'
		Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 12.0!)
		Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		Me.ClientSize = New System.Drawing.Size(381, 357)
		Me.Controls.Add(Me.Button2)
		Me.Controls.Add(Me.Label2)
		Me.Controls.Add(Me.Label1)
		Me.Controls.Add(Me.Button1)
		Me.Controls.Add(Me.MenuStrip1)
		Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
		Me.MainMenuStrip = Me.MenuStrip1
		Me.Name = "Form1"
		Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		Me.Text = "產生部門業績表小工具"
		Me.MenuStrip1.ResumeLayout(False)
		Me.MenuStrip1.PerformLayout()
		Me.ContextMenuStrip1.ResumeLayout(False)
		Me.ResumeLayout(False)
		Me.PerformLayout()

	End Sub

	Friend WithEvents Button1 As Button
    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents 設定ToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents 路徑設定ToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents 開啟檔案自動結束視窗ToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents Label1 As Label
    Friend WithEvents OpenFileDialog1 As OpenFileDialog
    Friend WithEvents NotifyIcon1 As NotifyIcon
    Friend WithEvents 離開ToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ContextMenuStrip1 As ContextMenuStrip
    Friend WithEvents OpenToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ExitToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents 不顯示小工具介面ToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents Label2 As Label
	Friend WithEvents Button2 As Button
	Friend WithEvents 資料設定ToolStripMenuItem As ToolStripMenuItem
End Class

<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form 覆寫 Dispose 以清除元件清單。
    <System.Diagnostics.DebuggerNonUserCode()> _
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
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Me.Button1 = New System.Windows.Forms.Button()
        Me.TBTo = New System.Windows.Forms.TextBox()
        Me.TBPort = New System.Windows.Forms.TextBox()
        Me.TBSend = New System.Windows.Forms.TextBox()
        Me.TBRcv = New System.Windows.Forms.TextBox()
        Me.Timer1 = New System.Windows.Forms.Timer(Me.components)
        Me.SuspendLayout()
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(105, 181)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(75, 23)
        Me.Button1.TabIndex = 0
        Me.Button1.Text = "Button1"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'TBTo
        '
        Me.TBTo.Location = New System.Drawing.Point(105, 88)
        Me.TBTo.Name = "TBTo"
        Me.TBTo.Size = New System.Drawing.Size(100, 22)
        Me.TBTo.TabIndex = 1
        '
        'TBPort
        '
        Me.TBPort.Location = New System.Drawing.Point(105, 116)
        Me.TBPort.Name = "TBPort"
        Me.TBPort.Size = New System.Drawing.Size(100, 22)
        Me.TBPort.TabIndex = 2
        '
        'TBSend
        '
        Me.TBSend.Location = New System.Drawing.Point(105, 144)
        Me.TBSend.Name = "TBSend"
        Me.TBSend.Size = New System.Drawing.Size(100, 22)
        Me.TBSend.TabIndex = 3
        '
        'TBRcv
        '
        Me.TBRcv.Location = New System.Drawing.Point(105, 274)
        Me.TBRcv.Name = "TBRcv"
        Me.TBRcv.Size = New System.Drawing.Size(100, 22)
        Me.TBRcv.TabIndex = 4
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 12.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(331, 365)
        Me.Controls.Add(Me.TBRcv)
        Me.Controls.Add(Me.TBSend)
        Me.Controls.Add(Me.TBPort)
        Me.Controls.Add(Me.TBTo)
        Me.Controls.Add(Me.Button1)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Button1 As Button
    Friend WithEvents TBTo As TextBox
    Friend WithEvents TBPort As TextBox
    Friend WithEvents TBSend As TextBox
    Friend WithEvents TBRcv As TextBox
    Friend WithEvents Timer1 As Timer
End Class

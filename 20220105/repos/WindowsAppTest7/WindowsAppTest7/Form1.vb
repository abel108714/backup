Public Class Form1
    Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Integer

    Declare Function FindWindowEx Lib "user32" Alias "FindWindowExA" _
    (ByVal hWndParent As Integer, ByVal hWndChildAfter As Integer, ByVal lpClassName As String, ByVal lpWindowName As String) As Integer

    Private Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As IntPtr) As Long
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim hwd1, hwd2 As IntPtr
        'hwd1 = FindWindow(vbNullString, "鼎新電腦 Cosmos ERP")
        hwd1 = FindWindow(vbNullString, "佇列工作控制台")
        SetForegroundWindow(hwd1)

        If hwd1.Equals(IntPtr.Zero) Then
            Label1.Text = "找不到"
        Else
            Label1.Text = "找到了"

            'hwd2 = FindWindowEx(hwd1, 0&, "Edit", vbNullString) '內容的視窗類別是Edit
            'If hwd2.Equals(IntPtr.Zero) Then
            ' Label2.Text = "找不到"
            ' Else
            ' Label2.Text = "找到了"
            ' End If

        End If
    End Sub
End Class


Public Class Form1
    'Private Declare Function SetCursorPos Lib "user32" (ByVal X As Long, ByVal Y As Long) As Long
    Declare Auto Function SetCursorPos Lib "user32" (ByVal x As Integer, ByVal y As Integer) As Integer
    'Private Declare Sub mouse_event Lib "user32" (ByVal dwFlags As Long, ByVal dx As Long, ByVal dy As Long, ByVal cButtons As Long, ByVal dwExtraInfo As Long)
    Declare Sub mouse_event Lib "user32" (ByVal dwFlags As Integer, ByVal dx As Integer, ByVal dy As Integer, ByVal dwData As Integer, ByVal dwExtraInfo As Integer)
    'Public Declare Function GetCursorPos Lib "user32" (ByRef lpPoint As POINTAPI) As Int32
    'Declare Function GetCursorPos Lib "user32" (ByVal X As Integer, ByVal Y As Integer) As Integer


    Declare Function RegisterHotKey Lib "user32" (ByVal hwnd As IntPtr, ByVal id As Integer, ByVal fsModifiers As Integer, ByVal vk As Long) As Integer
    Declare Function UnregisterHotKey Lib "user32" (ByVal hwnd As IntPtr, ByVal id As Integer) As Integer

    ' Handle the KeyDown event to print the type of character entered into the control.
    Private Sub TextBox1_KeyDown(sender As Object, e As KeyEventArgs) Handles TextBox1.KeyDown
        TextBox2.AppendText($"KeyDown code: {e.KeyCode}, value: {e.KeyValue}, modifiers: {e.Modifiers}" + vbCrLf)
    End Sub

    ' Handle the KeyPress event to print the type of character entered into the control.
    Private Sub TextBox1_KeyPress(sender As Object, e As KeyPressEventArgs) Handles TextBox1.KeyPress
        TextBox2.AppendText($"KeyPress keychar: {e.KeyChar}" + vbCrLf)
    End Sub

    ' Handle the KeyUp event to print the type of character entered into the control.
    Private Sub TextBox1_KeyUp(sender As Object, e As KeyEventArgs) Handles TextBox1.KeyUp
        TextBox2.AppendText($"KeyUp code: {e.KeyCode}, value: {e.KeyValue}, modifiers: {e.Modifiers}" + vbCrLf)
    End Sub

    Public Cont As Boolean = True

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load


        LetMeCallThread(sender, e)


    End Sub

    Dim KeyDowner1 As New KeyDown1()
    Dim Thread1 As New System.Threading.Thread(AddressOf KeyDowner1.Form_KeyDown)
    Dim DetCoorder1 As New DetCoord1()
    Dim Thread2 As New System.Threading.Thread(AddressOf DetCoorder1.detCoord)

    Private Sub LetMeCallThread(sender As Object, e As EventArgs)

        'Label1.Refresh()
        ' 與物件之間的Call Back機制, 建立handler (Call Back的function)
        ' 當物件Raise該事件時，可以透過該function取得結果
        AddHandler KeyDowner1.FinishedCounting, AddressOf FinishedCountingEventHandler1
        AddHandler DetCoorder1.FinishedCounting, AddressOf FinishedCountingEventHandler2
        ' 啟動執行緖
        While True
            Thread1.Start()
            Thread2.Start()


        End While
    End Sub
    Sub FinishedCountingEventHandler1(ByVal Cont As Integer)
        MsgBox(Cont)
    End Sub

    Sub FinishedCountingEventHandler2(ByVal coord As Integer)
        MsgBox(coord)
        Label1.Text = DetCoorder1.coord
        Label1.Refresh()
    End Sub
    Public Sub setLable1(s As String)
        Label1.Text = s
        Label1.Refresh()
    End Sub

End Class

Public Class KeyDown1
    Public Cont As Boolean = True
    Public Sub setContValue(b As Boolean)
        Cont = b
    End Sub
    Public Function getContValue()
        Return Cont
    End Function

    Public Event KeyDown(sender As Object, e As KeyEventArgs)
    Public Event FinishedCounting(ByVal NumberOfMatches As Integer)
    Private Sub Form_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown

        Select Case e.KeyCode
            Case Keys.Enter
                'Me.det(sender, e)
                'Me.TopMost = False
                setContValue(True)
                'Label2.Text = Cont
                'MsgBox(Cont)
                MsgBox("Enter")
            Case Keys.Space
                setContValue(False)
                'Label2.Text = Cont
                'MsgBox(Cont)
                'Me.Close()
                MsgBox("Space")
            Case Keys.Escape
                'Me.Close()
        End Select
        RaiseEvent FinishedCounting(Cont)
    End Sub
End Class

Public Class DetCoord1
    Public Const MOUSEEVENTF_LEFTDOWN = &H2
    Public Const MOUSEEVENTF_LEFTUP = &H4
    Public Const MOUSEEVENTF_MIDDLEDOWN = &H20
    Public Const MOUSEEVENTF_MIDDLEUP = &H40
    Public Const MOUSEEVENTF_RIGHTDOWN = &H8
    Public Const MOUSEEVENTF_RIGHTUP = &H10
    Public Const MOUSEEVENTF_MOVE = &H1

    Structure POINTAPI
        Dim x As Integer
        Dim y As Integer
    End Structure
    Declare Function GetCursorPos Lib "user32" Alias "GetCursorPos" (ByRef lpPoint As POINTAPI) As Integer

    Public coord As String
    Public Sub setCoordValue(s As String)
        coord = s
    End Sub
    Public Function getCoordValue()
        Return coord
    End Function
    Public Event FinishedCounting(ByVal NumberOfMatches As String)
    Private Sub detCoord(sender As Object, e As KeyEventArgs)
        Dim p As POINTAPI
        GetCursorPos(p)
        setCoordValue("p.x = " & p.x & " p.y = " & p.y)
        MsgBox(getCoordValue())
        Form1.setLable1(getCoordValue())
        RaiseEvent FinishedCounting(coord)
    End Sub
End Class
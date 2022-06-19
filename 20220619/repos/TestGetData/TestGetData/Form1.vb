Public Class Form1

    Declare Function GetParent Lib "user32" (ByVal hwnd As Long) As Long
    Declare Function GetWindowText Lib "user32" Alias "GetWindowTextA" (ByVal hwnd As Long, ByVal lpString As String, ByVal cch As Long) As Long
    Declare Function EnumWindows Lib "user32" (ByVal lpEnumFunc As Long, ByVal lParam As Long) As Long
    Declare Function GetWindowThreadProcessId Lib "user32" (ByVal hwnd As Long, lpdwProcessId As Long) As Long
    Declare Function GetClassName Lib "user32" Alias "GetClassNameA" (ByVal hwnd As Long, ByVal lpClassName As String, ByVal nMaxCount As Long) As Long
    Declare Function IsWindowVisible Lib "user32" (ByVal hwnd As Long) As Long

    Public coll As New Collection
    'Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
    'Dim nc As SomeClass = New SomeClass()
    'Show()

    'End Sub

    Dim PEC As New SomeClass



    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        'MsgBox(ListBox1.Text)
        PEC.SomeClass(ListBox1.Text)

    End Sub



    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click

        PEC.RunMsg()

        ListBox1.DataSource = PEC.getHandles

    End Sub


    Private Sub Command1_Click()
        Dim co As Object
        List1.Clear
        Call EnumWindows(AddressOf EnumWindowsProc)
        For Each co In coll
            If Mid(co, 1, 3) = "-!@" Then
                co = "Class Name:" + Mid(co, 4)
            End If
            List1.AddItem co
        Next
    End Sub

    Function EnumWindowsProc(ByVal hwnd As Long, ByVal lParam As Long) As Boolean
        Dim S As String, pid As Long
        If GetParent(hwnd) = 0 Then
            '讀取 hWnd 的視窗標題
            S = String(80, 0)
            Call GetWindowText(hwnd, S, 80)
            S = Left(S, InStr(S, Chr(0)) - 1)
            Call GetWindowThreadProcessId(hwnd, pid)
            '當沒有標題的hWnd之pid被加入Coll的Collection時，若pid重覆會有錯，我們不管它
            On Error Resume Next
            If Len(S) = 0 Then
                '沒有標題，則記錄Class Name
                S = String(255, 0)
                Call GetClassName(hwnd, S, 255)
                S = Left(S, InStr(S, Chr(0)) - 1)
                coll.Add "-!@" + S, Str(pid) 'key 為Pid
            Else
                '如果相同的pid記錄兩次，便會產生err, 而去執行errh的程式
                On Error GoTo errh
                If IsWindowVisible(hwnd) Then
                    coll.Add S, Str(pid)
      End If
            End If
        End If
        EnumWindowsProc = True ' 表示繼續列舉 hWnd
        Exit Function
errh:
        '如果先前coll 記錄key=pid的 那個Item記錄的是ClassName，則Item以Window
        '的Title來取代
        If Mid(coll.Item(Str(pid)), 1, 3) = "-!@" Then '表示先前以ClassName記錄
            coll.Remove(Str(pid))
            coll.Add S, Str(pid)
    End If
        EnumWindowsProc = True ' 表示繼續列舉 hWnd
    End Function
End Class


Public Class SomeClass

    Private myprocess As New System.Diagnostics.Process()

    Private lngPID, lParam As Long

    Private lngHWND As New ArrayList()

    Private lngRet As Long

    Private lngDesktopHWND As Long



    Public Delegate Function funcCallBackParent(ByVal hWnd As Long, ByVal lParam As Long) As Long

    Public Delegate Function funcCallBackChild(ByVal hWndParent As Long, ByVal lpEnumFunc As Long, ByVal lParam As Long) As Long

    Friend Declare Function EnumChildWindows Lib "User32" (ByVal hWndParent As Long, ByVal funcCallBack As funcCallBackChild, ByVal lParam As Long) As Long

    Friend Declare Function EnumWindows Lib "User32" (ByVal funcCallBack As funcCallBackParent, ByVal lParam As Long) As Long

    Public Declare Function GetDesktopWindow Lib "user32" () As Long



    Public Function getHandles() As ArrayList

        getHandles = lngHWND

    End Function



    Public Function getRetVal() As Long

        getRetVal = lngRet

    End Function



    Public Sub SomeClass(ByVal strPath As String)

        myprocess.StartInfo.FileName = "C:\Conductor\C_dsbin\MainMenu.exe"

        myprocess.StartInfo.Arguments = ""

        myprocess.Start()

    End Sub



    Public Sub RunMsg()

        Dim MyCallBack As New funcCallBackChild(AddressOf EnumChildWindowsProc)

        lngDesktopHWND = GetDesktopWindow()
        'MsgBox(lngDesktopHWND)
        lngPID = myprocess.Id
        'MsgBox(lngPID
        MsgBox(lngDesktopHWND)
        'MsgBox(MyCallBack)
        MsgBox(lParam)
        lngRet = EnumChildWindows(lngDesktopHWND, MyCallBack, lParam)
        'MsgBox(lngRet)
    End Sub



    Public Function EnumChildWindowsProc(ByVal hWndParent As Long, ByVal lpEnumFunc As Long, ByVal lParam As Long) As Long

        lngHWND.Add(hWndParent)

        EnumChildWindowsProc = 1

    End Function

End Class
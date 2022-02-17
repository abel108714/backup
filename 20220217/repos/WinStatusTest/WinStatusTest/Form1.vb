Option Strict Off
Option Explicit On
Friend Class Form1
    Inherits System.Windows.Forms.Form

    Private Structure POINTAPI
        Dim x As Integer
        Dim y As Integer
    End Structure

    Private Structure RECT
        Dim Left_Renamed As Integer
        Dim Top_Renamed As Integer
        Dim Right_Renamed As Integer
        Dim Bottom_Renamed As Integer
    End Structure

    Private Structure WINDOWPLACEMENT
        Dim Length As Integer
        Dim flags As Integer
        Dim showCmd As Integer
        Dim ptMinPosition As POINTAPI
        Dim ptMaxPosition As POINTAPI
        Dim rcNormalPosition As RECT
    End Structure

    Private Enum WinMode
        Normal = 1 ' 一般
        Maxmize = 3 ' 最大
        Minimize = 6 ' 最小
    End Enum

    Private Const SW_SHOWMINIMIZED As Short = 2
    Private Const SW_SHOWMAXIMIZED As Short = 3
    Private Const SW_SHOWNORMAL As Short = 1

    Private Declare Function SetWindowPlacement Lib "user32" (ByVal hwnd As Integer, ByRef lpwndpl As WINDOWPLACEMENT) As Integer
    Private Declare Function GetWindowPlacement Lib "user32" (ByVal hwnd As Integer, ByRef lpwndpl As WINDOWPLACEMENT) As Integer
    Private Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As Integer) As Integer
    Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Integer

    Private Sub Ctrl_Win_State(ByRef strWin As String, ByRef mode As WinMode)
        Dim intWnd As Integer
        Dim CurWinP As WINDOWPLACEMENT
        Dim p() As Process = System.Diagnostics.Process.GetProcessesByName(strWin)
        If p.Length > 0 Then
            intWnd = p(0).MainWindowHandle
            GetWindowPlacement(intWnd, CurWinP)
            CurWinP.Length = Len(CurWinP)
            CurWinP.flags = 0
            CurWinP.showCmd = mode
            SetWindowPlacement(intWnd, CurWinP)
            SetForegroundWindow(intWnd)
        Else
            intWnd = FindWindow(vbNullString, strWin)
            GetWindowPlacement(intWnd, CurWinP)
            CurWinP.Length = Len(CurWinP)
            CurWinP.flags = 0
            CurWinP.showCmd = mode
            SetWindowPlacement(intWnd, CurWinP)
            SetForegroundWindow(intWnd)
        End If
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        '法1
        'Ctrl_Win_State("Microsoft Excel - 門市部日報表20200714_085047", WinMode.Maxmize) ' 
        '法2
        Ctrl_Win_State("excel", WinMode.Minimize) ' 
    End Sub

End Class


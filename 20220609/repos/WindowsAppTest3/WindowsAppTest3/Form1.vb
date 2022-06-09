Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        LetMeCallThread(1 + 2 + 3 + 4)
    End Sub
    ' 這一段程式碼就是用來執行呼叫thread
    Dim counter1 As New Count1()
    Dim Thread1 As New System.Threading.Thread(AddressOf counter1.Count)
    Private Sub LetMeCallThread(ByVal counter As Integer)
        counter1.CountTo = counter
        ' 與物件之間的Call Back機制, 建立handler (Call Back的function)
        ' 當物件Raise該事件時，可以透過該function取得結果
        AddHandler counter1.FinishedCounting, AddressOf FinishedCountingEventHandler
        ' 啟動執行緖
        Thread1.Start()
    End Sub

    '  當Thread程式執行完畢(這就是所謂的CallBack機制)
    Sub FinishedCountingEventHandler(ByVal Count As Integer)
        MsgBox(Count)
    End Sub
End Class

'  這類別沒什麼特別的，只是做一個簡單的For Loop加總 
Public Class Count1
    Public CountTo As Integer
    '  當程序處理完畢，透過這個method來讓對方知道你已經做完了
    Public Event FinishedCounting(ByVal NumberOfMatches As Integer)
    Sub Count()
        Dim ind, tot As Integer
        tot = 0
        For ind = 1 To CountTo
            tot += 1
        Next ind
        ' raise一個事件出來說已經做完了
        ' 並將處理完的值回傳回去
        RaiseEvent FinishedCounting(tot)
    End Sub
End Class
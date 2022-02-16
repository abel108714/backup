Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.Hide()
        Me.Visible = False
        Main()
    End Sub
    Private Sub Form1_Activated(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Activated
        Me.Hide()
        Me.Visible = False
    End Sub
    Public Shared Sub Main()
        Console.WriteLine()
        '  Invoke this sample with an arbitrary set of command line arguments.
        Dim arguments As String() = Environment.GetCommandLineArgs()
        Console.WriteLine("GetCommandLineArgs: {0}", String.Join(", ", arguments))
    End Sub
End Class

Class Sample

End Class

Imports System

Module Program
	Sub Main(ByVal ParamArray args() As String)
		Dim i As Integer
		For i = 0 To UBound(args)
			Console.WriteLine("args " & i & args(i))
		Next i
	End Sub
End Module



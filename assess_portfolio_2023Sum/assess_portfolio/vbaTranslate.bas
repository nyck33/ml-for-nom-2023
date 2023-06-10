
Dim A as Integer
B = 20

Sub DotIt(X as Double)
    Select Case A
        Case 1
            B = B + X
        Case 2
            B = B - X
        Case Else
            B = 0
    End Select
End Sub

Function GetHalfB() As Integer
    GetHalfB = B / 2
End Function
    
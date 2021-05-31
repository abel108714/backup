Attribute VB_Name = "Module3"
Dim datastart As Integer, rd_start As Integer, startRow As Integer
'Set ws1 = Sheets("worksheet1")
'Set ws2 = Sheets("number2")
Dim Str() As String, s() As String

Sub 網通部門業績表()
    Sheets("Sheet1").Cells.Clear
    'Sheets("Sheet1").Cells.Delete Shift:=xlUp
    Sheets("Sheet1").Cells.ClearContents
    Set xSh = Worksheets("Sheet1")
    With xSh
        .Cells.UseStandardHeight = True
        .Cells.UseStandardWidth = True
    End With
    Dim rSou As Range, rTar As Range
    Set rSou = Sheets("報表 1").Range("A1:Q3")
    Set rTar = Sheets("Sheet1").Range("A1:Q3")
    rSou.Copy rTar
    With rTar
        rSou.Copy
        .PasteSpecial Paste:=xlPasteColumnWidths, Operation:=xlNone, _
                      SkipBlanks:=False, Transpose:=False
        .PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, _
                      SkipBlanks:=False, Transpose:=False
    End With
    Worksheets("報表 1").Range("A1:A3").EntireRow.Copy Destination:=Worksheets("Sheet1").Range("A1:A3").EntireRow
   
    Dim dept As String
    Dim rd_row() As String, osc_row() As String, st_row() As String, pd_row() As String, pj_row() As String
   
    Dim osc_start As Integer, st_start As Integer, pd_start As Integer, pj_start As Integer

    Dim startRow As Integer
    datastart = 4
    rd_start = datastart
    With Application.FindFormat
        .Font.ColorIndex = 3
    End With
    dept = "網通"   '設定專屬部門名稱
    With Worksheets("報表 1").Range("D:D") '先找出，標記各部門的所在列數
        Set rd = .Find("開發", LookIn:=xlValues, SearchFormat:=True)
        rd_addr = rd.Address
        rd_row = Split(rd_addr, "$")
        osc_start = rd_row(2) + 1
        'MsgBox osc_start
        Set osc = .Find("網通", LookIn:=xlValues, SearchFormat:=True)
        osc_addr = osc.Address
        osc_row = Split(osc_addr, "$")
        st_start = osc_row(2) + 1
        'MsgBox st_start
        Set st = .Find("門市", LookIn:=xlValues, SearchFormat:=True)
        st_addr = st.Address
        st_row = Split(st_addr, "$")
        pd_start = st_row(2) + 1
        'MsgBox pd_start
        Set pd = .Find("胖老爺", LookIn:=xlValues, SearchFormat:=True)
        pd_addr = pd.Address
        pd_row = Split(pd_addr, "$")
        pj_start = pd_row(2) + 1
        'MsgBox pj_start
        Set pj = .Find("專案", LookIn:=xlValues, SearchFormat:=True)
        pj_addr = pj.Address
        pj_row = Split(pj_addr, "$")
        'MsgBox pj_row
       
    End With

   

    '複製內容


    Dim arrResult() As Integer
   
   
    Dim Data_row_tail As Integer
    Dim i As Integer
    i = 0
    With Worksheets("報表 1").Range("D:D")

        Set c = .Find(dept, LookIn:=xlValues, SearchFormat:=True)

        If Not c Is Nothing Then
       
            firstAddress = c.Address
            'FirstAddresscolor = c.Font.Color
            Str = Split(c.Address, "$")

           
            newAddress = Str(2) - getStartRow(dept)
            'MsgBox "Str(2) = " & Str(2)
            'MsgBox "getStartRow(dept) = " & getStartRow(dept)
            'MsgBox "c.Address = " & c.Address
            'MsgBox "newAddress = " & newAddress
            '複製內容
            Worksheets("報表 1").Range("D" & getStartRow(dept) & ":" & c.Address).EntireRow.Copy Destination:=Worksheets("Sheet1").Range("4" & ":" & 4 + newAddress).EntireRow
           
        End If
    End With

    newAddress = Str(2) - getStartRow(dept)
    '最後一行空白
    Worksheets("Sheet1").Range(4 + newAddress + 1 & ":" & 4 + newAddress + 1).Borders.Color = vbWhite
    Worksheets("Sheet1").Range(4 + newAddress + 1 & ":" & 4 + newAddress + 1).RowHeight = Worksheets("報表 1").Range(4 + newAddress + 1 & ":" & 4 + newAddress + 1).RowHeight * 2
   
End Sub

Function getStartRow(dept As String)

    With Application.FindFormat
        .Font.ColorIndex = 3
    End With

    With Worksheets(1).Range("D:D") '先找出，標記各部門的所在列數

        Set rd = .Find("開發", LookIn:=xlValues, SearchFormat:=True)
        rd_addr = rd.Address

        rd_row = Split(rd_addr, "$")
        osc_start = rd_row(2) + 1

        Set osc = .Find("網通", LookIn:=xlValues, SearchFormat:=True)
        osc_addr = osc.Address
        osc_row = Split(osc_addr, "$")
        st_start = osc_row(2) + 1

        Set st = .Find("門市", LookIn:=xlValues, SearchFormat:=True)
        st_addr = st.Address
        st_row = Split(st_addr, "$")
        pd_start = st_row(2) + 1

        Set pd = .Find("胖老爺", LookIn:=xlValues, SearchFormat:=True)
        pd_addr = pd.Address
        pd_row = Split(pd_addr, "$")
        pj_start = pd_row(2) + 1

        Set pj = .Find("專案", LookIn:=xlValues, SearchFormat:=True)
        pj_addr = pj.Address
        pj_row = Split(pj_addr, "$")
       
    End With
   
    If dept = "開發" Then
        startRow = rd_start
    ElseIf dept = "網通" Then
        startRow = osc_start
    ElseIf dept = "門市" Then
        startRow = st_start
    ElseIf dept = "胖老爺" Then
        startRow = pd_start
    ElseIf dept = "專案" Then
        startRow = pj_start
    End If

    getStartRow = startRow
   
End Function





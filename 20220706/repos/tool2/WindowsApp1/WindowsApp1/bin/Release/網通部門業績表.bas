Attribute VB_Name = "Module3"
Dim datastart As Integer, rd_start As Integer, startRow As Integer
'Set ws1 = Sheets("worksheet1")
'Set ws2 = Sheets("number2")
Dim Str() As String, s() As String

Sub ���q�����~�Z��()
    Sheets("Sheet1").Cells.Clear
    'Sheets("Sheet1").Cells.Delete Shift:=xlUp
    Sheets("Sheet1").Cells.ClearContents
    Set xSh = Worksheets("Sheet1")
    With xSh
        .Cells.UseStandardHeight = True
        .Cells.UseStandardWidth = True
    End With
    Dim rSou As Range, rTar As Range
    Set rSou = Sheets("���� 1").Range("A1:Q3")
    Set rTar = Sheets("Sheet1").Range("A1:Q3")
    rSou.Copy rTar
    With rTar
        rSou.Copy
        .PasteSpecial Paste:=xlPasteColumnWidths, Operation:=xlNone, _
                      SkipBlanks:=False, Transpose:=False
        .PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, _
                      SkipBlanks:=False, Transpose:=False
    End With
    Worksheets("���� 1").Range("A1:A3").EntireRow.Copy Destination:=Worksheets("Sheet1").Range("A1:A3").EntireRow
   
    Dim dept As String
    Dim rd_row() As String, osc_row() As String, st_row() As String, pd_row() As String, pj_row() As String
   
    Dim osc_start As Integer, st_start As Integer, pd_start As Integer, pj_start As Integer

    Dim startRow As Integer
    datastart = 4
    rd_start = datastart
    With Application.FindFormat
        .Font.ColorIndex = 3
    End With
    dept = "���q"   '�]�w�M�ݳ����W��
    With Worksheets("���� 1").Range("D:D") '����X�A�аO�U�������Ҧb�C��
        Set rd = .Find("�}�o", LookIn:=xlValues, SearchFormat:=True)
        rd_addr = rd.Address
        rd_row = Split(rd_addr, "$")
        osc_start = rd_row(2) + 1
        'MsgBox osc_start
        Set osc = .Find("���q", LookIn:=xlValues, SearchFormat:=True)
        osc_addr = osc.Address
        osc_row = Split(osc_addr, "$")
        st_start = osc_row(2) + 1
        'MsgBox st_start
        Set st = .Find("����", LookIn:=xlValues, SearchFormat:=True)
        st_addr = st.Address
        st_row = Split(st_addr, "$")
        pd_start = st_row(2) + 1
        'MsgBox pd_start
        Set pd = .Find("�D�ѷ�", LookIn:=xlValues, SearchFormat:=True)
        pd_addr = pd.Address
        pd_row = Split(pd_addr, "$")
        pj_start = pd_row(2) + 1
        'MsgBox pj_start
        Set pj = .Find("�M��", LookIn:=xlValues, SearchFormat:=True)
        pj_addr = pj.Address
        pj_row = Split(pj_addr, "$")
        'MsgBox pj_row
       
    End With

   

    '�ƻs���e


    Dim arrResult() As Integer
   
   
    Dim Data_row_tail As Integer
    Dim i As Integer
    i = 0
    With Worksheets("���� 1").Range("D:D")

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
            '�ƻs���e
            Worksheets("���� 1").Range("D" & getStartRow(dept) & ":" & c.Address).EntireRow.Copy Destination:=Worksheets("Sheet1").Range("4" & ":" & 4 + newAddress).EntireRow
           
        End If
    End With

    newAddress = Str(2) - getStartRow(dept)
    '�̫�@��ť�
    Worksheets("Sheet1").Range(4 + newAddress + 1 & ":" & 4 + newAddress + 1).Borders.Color = vbWhite
    Worksheets("Sheet1").Range(4 + newAddress + 1 & ":" & 4 + newAddress + 1).RowHeight = Worksheets("���� 1").Range(4 + newAddress + 1 & ":" & 4 + newAddress + 1).RowHeight * 2
   
End Sub

Function getStartRow(dept As String)

    With Application.FindFormat
        .Font.ColorIndex = 3
    End With

    With Worksheets(1).Range("D:D") '����X�A�аO�U�������Ҧb�C��

        Set rd = .Find("�}�o", LookIn:=xlValues, SearchFormat:=True)
        rd_addr = rd.Address

        rd_row = Split(rd_addr, "$")
        osc_start = rd_row(2) + 1

        Set osc = .Find("���q", LookIn:=xlValues, SearchFormat:=True)
        osc_addr = osc.Address
        osc_row = Split(osc_addr, "$")
        st_start = osc_row(2) + 1

        Set st = .Find("����", LookIn:=xlValues, SearchFormat:=True)
        st_addr = st.Address
        st_row = Split(st_addr, "$")
        pd_start = st_row(2) + 1

        Set pd = .Find("�D�ѷ�", LookIn:=xlValues, SearchFormat:=True)
        pd_addr = pd.Address
        pd_row = Split(pd_addr, "$")
        pj_start = pd_row(2) + 1

        Set pj = .Find("�M��", LookIn:=xlValues, SearchFormat:=True)
        pj_addr = pj.Address
        pj_row = Split(pj_addr, "$")
       
    End With
   
    If dept = "�}�o" Then
        startRow = rd_start
    ElseIf dept = "���q" Then
        startRow = osc_start
    ElseIf dept = "����" Then
        startRow = st_start
    ElseIf dept = "�D�ѷ�" Then
        startRow = pd_start
    ElseIf dept = "�M��" Then
        startRow = pj_start
    End If

    getStartRow = startRow
   
End Function





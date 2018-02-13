Sub medium()
  Dim tickerName As String
  Dim prevTicker As String
  Dim volumeTotal As Double
  volumeTotal = 0
  ' row index in summary table
  Dim SumRow As Integer
  SumRow = 2
  ' Loop through all credit card purchases
  Dim lastRow As Long
  Dim minDateRow As Long
  Dim maxDateRow As Long
  Dim change As Double
  
  lastRow = Cells(Rows.Count, 1).End(xlUp).Row
  'Debug.Print (lastRow)
  prevTicker = Cells(2, 1).Value
  prevDate = Cells(2, 2).Value
  minDateRow = 2
  
  Dim ws As Worksheet
  Set ws = Application.ActiveSheet
  
  For i = 2 To lastRow + 1
    tickerName = Cells(i, 1).Value
    ' Debug.Print (i)
    If tickerName = prevTicker Then
      'Add to the Brand Total
      volumeTotal = volumeTotal + Cells(i, 7).Value
      If Cells(i, 2).Value < prevDate Then
            prevDate = Cells(i, 2).Value
            minDateRow = i
            
      ElseIf Cells(i, 2).Value > prevDate Then
            prevDate = Cells(i, 2).Value
            maxDateRow = i
            
      Else
      End If
    Else
      ' Print the Credit Card Brand in the Summary Table
      Cells(1, 10).Value = "Ticker"
      Cells(1, 11).Value = "Yearly Change"
      Cells(1, 12).Value = "Yearly Pecent Change"
      Cells(1, 13).Value = "Volume"
      lastSumRow = Cells(Rows.Count, 10).End(xlUp).Row
      
      ' Print ticker label
      Range("J1:N100").Cells(SumRow, 1).Value = prevTicker
      ' Print the Brand Amount to the Summary Table
      Range("J1:N100").Cells(SumRow, 4).Value = volumeTotal
      
      ' Print Yearly Change
      'Debug.Print ("Min" & minDateRow)
      'Debug.Print ("Max" & maxDateRow)
      'Debug.Print (Cells(maxDateRow, 6).Value)
      'Debug.Print (Cells(minDateRow, 3).Value)
      change = Cells(maxDateRow, 6).Value - Cells(minDateRow, 3).Value
      
      'Debug.Print (change)
      Range("J1:N100").Cells(SumRow, 2).Value = change
        If Cells(SumRow, 11).Value > 0 Then
            Cells(SumRow, 11).Interior.ColorIndex = 4
        ElseIf Cells(SumRow, 11).Value < 0 Then
            Cells(SumRow, 11).Interior.ColorIndex = 3
        Else
        End If
      
      ' Print Yearly Percent Change
      If Cells(minDateRow, 3).Value <> 0 Then
        Range("J1:N100").Cells(SumRow, 3).Value = change / Cells(minDateRow, 3).Value
        Range("L2:L" & lastSumRow).NumberFormat = "0.00%"
      Else
        Range("J1:N100").Cells(SumRow, 3).Value = "NA"
      End If
      
      ' Add one to the summary table row
      SumRow = SumRow + 1
      ' Start the new Brand Total
      volumeTotal = Cells(i, 3).Value
      prevTicker = tickerName
    End If
  Next i
  

End Sub

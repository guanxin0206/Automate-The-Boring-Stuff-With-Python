#!python3
# Table Printer Practice Project on Automate the boring stuff with python chapter 6

tableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
  colWidths = [0] * len(tableData)
  for i, item in enumerate(tableData):
    #for s in item:
    colWidths[i] = len(max(item,key=len))
      
  width = max(colWidths)
  
  for i in range(0,len(tableData[0])):
    
    print(tableData[0][i].rjust(width),end=' ')
    print(tableData[1][i].rjust(width),end=' ')
    print(tableData[2][i].rjust(width),end=' ')
    print('')

printTable(tableData)


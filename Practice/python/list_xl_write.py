import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
listdata = [99,92,93,94,95,96,97,98,99,100]
row = 0
for l in listdata:
    col = 0
    print row,col
    sheet1.write(row, col, l)
    row+=1
    print l,col
        
book.save("tfile1.xls")
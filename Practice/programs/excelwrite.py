import xlwt

wb = xlwt.Workbook()
sht1 = wb.add_sheet("sheetone")
sht2 = wb.add_sheet("sheettwo")

for row in range(16):
    for col in range(1):
        sht1.write(row,col,"test- "+(str(row)))
        sht2.write(row,col,"test- "+(str(row)))
        print str(row)


wb.save("exwritre2.xls")

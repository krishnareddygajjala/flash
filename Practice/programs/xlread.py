import xlrd
#import xlwt



xlwb = xlrd.open_workbook(r"C:\Users\Ram\git\flash\Practice\programs\exwritre2.xls")
shname = xlwb.sheet_names()
print shname
for i in range(len(shname)):
    xlsheet = xlwb.sheet_by_index(i)
    row = xlsheet.nrows
    col = xlsheet.ncols
    print row,col
    for i in range(row):
        for j in range(col):
            cell_obj = xlsheet.cell(i,j)
            print cell_obj
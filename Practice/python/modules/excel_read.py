
import xlrd

xlwb = xlrd.open_workbook(r"C:\Users\Ram\git\flash\Practice\python\modules\fakedata1.xls")
shname = xlwb.sheet_names()
#print shname[0]
file=open("data123.txt","w")
for i in range(len(shname)):
    xlsheet = xlwb.sheet_by_index(i)
    row = xlsheet.nrows
    col = xlsheet.ncols
    #print row,col
    for i in range(row):
        for j in range(1):
            name = xlsheet.cell_value(i,j)
            email = xlsheet.cell_value(i,1)
            password = xlsheet.cell_value(i,2)
            country = xlsheet.cell_value(i,3)            
#             print name.value
#             print email.value
#             print password.value
#             print country.value
            file.write(name+" - "+email+" - "+password+" - "+country+" \n")
            print "%s - %s -%s -%s"%(name,email,password,country)
file.close()
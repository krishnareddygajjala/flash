import xlwt
from faker import Faker

fake = Faker()
book = xlwt.Workbook(encoding="ASCII")
sheet1 = book.add_sheet("Sheet_12")

row = 0
for l in range(50):
    col = 0
    name = fake.name()
    email = fake.email()
    password = fake.password()
    country = fake.country()
    sheet1.write(row, col, name)
    sheet1.write(row,col+1,email)
    sheet1.write(row,col+2,password)
    sheet1.write(row,col+3,country)
    row+=1
        
book.save("fakedata1.xls")
print "sucess"
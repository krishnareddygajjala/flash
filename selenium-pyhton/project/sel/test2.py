import xlwt
import xlrd
from selenium import webdriver
#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.facebook.com/")

xlwb = xlrd.open_workbook(r"C:\Users\Ram\git\flash\selenium-pyhton\project\sel\sample1.xls")
shname = xlwb.sheet_names()

wb = xlwt.Workbook(encoding="utf-8")
sht = wb.add_sheet("sheetone")

element = driver.find_element_by_id("month")
all_options = element.find_elements_by_tag_name("option")
try:
    row = 0
    for option in all_options: 
        print("Value is: %s" % option.get_attribute("innerHTML"))
        col = 0
        sht.write(row,col,option.get_attribute("innerHTML"))
        col+=1
        row+=1 
            
except Exception,error:
    print error,Exception
    print "there is a error in try block"
wb.save("xlwrtfile0.xls")

for i in range(len(shname)):
    xlsheet = xlwb.sheet_by_index(i)
    row = xlsheet.nrows
    col = xlsheet.ncols
    print row,col
    for i in range(row):
        for j in range(col):
            cell_obj = xlsheet.cell(i,j)
            print str(cell_obj)
    
driver.quit()

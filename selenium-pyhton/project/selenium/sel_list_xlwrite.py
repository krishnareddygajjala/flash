import xlwt
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.facebook.com/")
wb = xlwt.Workbook()
sht = wb.add_sheet("sheetone")

element = driver.find_element_by_id("month")
all_options = element.find_elements_by_tag_name("option")
row = 0
for option in all_options: 
    print("Value is: %s" % option.get_attribute("innerHTML"))
    col = 0
    sht.write(row,col,option.get_attribute("innerHTML"))
    col+=1
    row+=1 
wb.save("writelst.xls")

driver.quit()
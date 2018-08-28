
import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.goibibo.com/")
driver.set_page_load_timeout(30)
print driver.title
adate = '11-July-2018'
time.sleep(5)
cal_textbox = driver.find_element_by_xpath("//input[@class='form-control inputTxtLarge widgetCalenderTxt']")
cal_textbox.click()
time.sleep(5)
next_month  = driver.find_element_by_xpath("//span[@class='DayPicker-NavButton DayPicker-NavButton--next']")
month_title = driver.find_elements_by_xpath("//div[@class='DayPicker-Month']/div[@role='heading']")

time.sleep(5)
for i in month_title:
    if 'July' not in i.get_attribute("innerHTML"):
        next_month.click()
        print i.get_attribute("innerHTML")
        
previous_month = driver.find_element_by_xpath("//span[@class='DayPicker-NavButton DayPicker-NavButton--prev']") 
day = driver.find_elements_by_xpath("//div[@class='DayPicker-Month']/div[@class='DayPicker-Body']/div/div/div")
time.sleep(5)   
for i in day:
    if '11' in i.get_attribute("innerHTML"):
        print i.get_attribute("innerHTML")
        i.click()

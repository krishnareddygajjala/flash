
import time 
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.facebook.com/")
print driver.title
driver.find_element_by_xpath("//input[@id='email']").send_keys("krishna")
driver.find_element_by_xpath("//input[@id='pass']").send_keys("password")

driver.find_element_by_name("firstname").send_keys("krishna")
driver.find_element_by_name("lastname").send_keys("reddy")
driver.find_element_by_name("reg_email__").send_keys("9949292929")
driver.find_element_by_name("reg_passwd__").send_keys("dontask123")
# initialize Select object
year = Select(driver.find_element_by_id("year"))
year.select_by_value("1989")

day = Select(driver.find_element_by_id("day"))
day.select_by_value("10")

month = Select(driver.find_element_by_id("month"))
month.select_by_value("10")
driver.find_element_by_xpath("//input[@value='2' and @name='sex']").click()
assert 'Facebook' in driver.title
time.sleep(10)
driver.quit()

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")

driver.get("http://www.gcrit.com/build3/create_account.php")
driver.find_element_by_xpath("//input[@name='gender' and @value='m']").click()
time.sleep(10)
driver.close()
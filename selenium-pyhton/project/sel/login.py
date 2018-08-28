
import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Python27\chromedriver.exe")
driver.get(" http://34.205.159.112/admin/login/?next=/admin/")
driver.implicitly_wait(20)
time.sleep(10)

driver.find_element_by_id("id_username").send_keys("totient")
driver.find_element_by_id("id_password").send_keys("test123!")
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(5)
driver.close()


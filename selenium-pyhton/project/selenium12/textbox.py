import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")

driver.get("http://www.gcrit.com/build3/create_account.php")
driver.find_element_by_name("firstname").send_keys("krishna")
driver.find_element_by_name("lastname").send_keys("reddy")
#driver.find_element_by_name("confirmation").send_keys("krishna")

time.sleep(10)
driver.close()
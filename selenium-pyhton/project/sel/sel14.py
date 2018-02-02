from selenium import webdriver
from time import time
 
driver = webdriver.Chrome(executable_path="F:\selenium required software\selenium drivers\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
#driver.maximize_window()
driver.implicitly_wait(10)
print driver.title
#driver.find_element_by_id("search_query_top").send_keys("printed dress")
driver.find_element_by_class_name("cat-title").click()

time().sleep(10)
driver.close()
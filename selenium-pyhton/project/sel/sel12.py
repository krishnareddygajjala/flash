from selenium import webdriver
from time import time 

driver = webdriver.Chrome(executable_path="F:\selenium required software\selenium drivers\chromedriver.exe")
driver.get("https://www.google.co.in")
#driver.maximize_window()
driver.implicitly_wait(10)
driver.save_screenshot("google.png")
driver.find_element_by_id("lst-ib").send_keys("python selenium")
print (driver.current_url)
print (time())
driver.close()

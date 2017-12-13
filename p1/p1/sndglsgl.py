from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.google.co.in")
driver.maximize_window()
driver.implicitly_wait(10)
title = driver.title
print title
driver.find_element_by_id("lst-ib").send_keys("python")
driver.find_element_by_name("btnK").click()

time.sleep(10)
driver.close()



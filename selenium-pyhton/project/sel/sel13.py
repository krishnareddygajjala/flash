from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\selenium required software\selenium drivers\chromedriver.exe")
driver.get("https://www.google.co.in/")
print driver.title
print driver.current_url
print driver.name
#print driver.page_source

time.sleep(5)
driver.quit()
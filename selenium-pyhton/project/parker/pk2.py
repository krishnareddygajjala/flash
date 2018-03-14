
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://ph.parker.com/in/en/CreateAccount?myAcctMain=1&new=Y")
time.sleep(10)


driver.find_element_by_xpath("//div[@class='dropdown custom_dropdown open']/button")
allops=driver.find_elements_by_xpath("//div/ul/li[@role='presentation']")
for i in allops:
    print i.get_attribute("innerHTML")


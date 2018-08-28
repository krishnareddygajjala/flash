
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://ph.parker.com/in/en/CreateAccount?myAcctMain=1&new=Y")
driver.maximize_window()
time.sleep(10)
driver.find_element_by_xpath("//input[@id='searchString']").send_keys("BST-N")
time.sleep(5)
lis = driver.find_elements_by_xpath("//ul[@class='typeahead__list']/li/a/span") 
time.sleep(5)
print len(lis)

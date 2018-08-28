import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://parker.com/")
driver.maximize_window()
time.sleep(10)

driver.find_element_by_xpath("//input[@id='keyWord']").send_keys("BST-N")
time.sleep(10)
lis = driver.find_elements_by_xpath("//ul[@class='typeahead__list']/li/a/span") 
time.sleep(5)
print len(lis)

for i in lis:
    print i.get_attribute("innerHTML")
    time.sleep(1)
    if '4' in i.get_attribute("innerHTML"):
        i.click()
        break
time.sleep(10)

titl = driver.find_elements_by_xpath("//div[@id='search-results']/div/a/div[2]/h6/span")
for i in titl:
    print i.get_attribute("innerHTML")


time.sleep(15)
driver.close()
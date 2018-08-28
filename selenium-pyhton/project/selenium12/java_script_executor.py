
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys

chrome_options = Options()

#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notificationss")
#chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.redbus.in/")
print driver.title
#driver.maximize_window()
time.sleep(5)

#driver.execute_script("document.getElementById('src').value='Bangalore'")

driver.find_element_by_id('src').send_keys('ban')
time.sleep(5)
lis = driver.find_elements_by_xpath("//section [@id='search']/div/div[2]/div/ul/li") 
print len(lis)
for i in lis:
    print i.get_attribute("innerHTML")
    time.sleep(1)
    if i.get_attribute("innerHTML") == "Bangalore":
        i.click()
        break

driver.find_element_by_xpath("//input[@id='dest']").send_keys("ka")
time.sleep(5)
lis = driver.find_elements_by_xpath("//section [@id='search']/div/div[2]/div/ul/li") 
print len(lis)
for i in lis:
    print i.get_attribute("innerHTML")
    time.sleep(1)
    if i.get_attribute("innerHTML") == "Kadapa":
        i.click()
        break
driver.set_script_timeout(5)
driver.execute_script("document.getElementById('onward_cal').value='28-May-2018'")
driver.find_element_by_xpath("//button[@id='search_btn']").click()
print "over"


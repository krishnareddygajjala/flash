
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notificationss")
#chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://www.globalsqa.com/demo-site/frames-and-windows/")
driver.set_page_load_timeout(30)
time.sleep(10)
driver.maximize_window()
tab1 = driver.find_element_by_xpath("//div[@rel-title='Open New Tab']/a[text()='Click Here']")
tab2 = driver.find_element_by_xpath("//div[@rel-title='Open New Tab']/a[text()='Click Here']")
tab3 = driver.find_element_by_xpath("//div[@rel-title='Open New Tab']/a[text()='Click Here']")
tab1.click()
time.sleep(5)
tab2.click()
time.sleep(5)
tab3.click()
time.sleep(3)
#driver.execute_script("window.open()")

#cookie = {'name' : 'foo', 'value' : 'bar'}
#driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
#print driver.get_cookies()

handles = driver.window_handles
size = len(handles)
print size

# driver.switch_to.window(handles[0])
# print driver.title
# time.sleep(5)
# driver.switch_to.window(handles[2])
# print driver.title
# time.sleep(5)
# driver.switch_to.window(handles[3])
# print driver.title

for x in range(size):
    driver.switch_to.window(handles[x])
    print driver.title
# 
# for handle in driver.window_handles:
#     print "Handle = ",handle
#     driver.switch_to.window(handle)
#     print driver.title
    
driver.quit()


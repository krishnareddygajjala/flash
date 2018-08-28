
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
#chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.redbus.in/")
print driver.title
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//i[@id='i-icon-profile']").click()
driver.find_element_by_xpath("//li[@id='signInLink']").click()
frame = driver.find_element_by_xpath("//iframe[@class='modalIframe']")
driver.switch_to_frame(frame)
time.sleep(10)
driver.find_element_by_xpath("//button[@class='action-button signup-screen signup-btn']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='emailID']").send_keys("krishnaredbus@gmail.com")
driver.find_element_by_xpath("//div/input[@id='password' and @class='IP']").send_keys("redbus420")
driver.find_element_by_xpath("//button[@id='createAccountLink']").click()
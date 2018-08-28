
     
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--enable-automation")
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-geolocation")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.redbus.in/")
print driver.title
time.sleep(15)
driver.close()
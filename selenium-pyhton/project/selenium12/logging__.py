import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys

print os.getcwd()
os.chdir("C:\Users\Ram\Desktop")
print os.getcwd()
log_filename = "example1.log"
logging.basicConfig(filename=log_filename,level = logging.DEBUG)
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notificationss")
#chrome_options.add_argument("--incognito")
logging.info("added chrome arguments")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://www.google.co.in")
logging.debug("opened google search page")
print driver.title
time.sleep(5)

driver.close()
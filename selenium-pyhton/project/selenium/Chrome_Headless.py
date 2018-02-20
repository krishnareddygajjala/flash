
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://www.google.co.in")
print driver.title
driver.get_screenshot_as_file("C:\Users\Ram\Desktop\krishna.png")
print "headless browser is closing"
driver.close()



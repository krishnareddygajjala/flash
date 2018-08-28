
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()

#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notificationss")
#chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.amazon.in/")
print driver.title
driver.maximize_window()
time.sleep(5)

a = driver.find_element_by_xpath("//a[@id='nav-link-shopall']/span[1]")
b= driver.find_element_by_xpath("//div[@id='nav-flyout-shopAll']/div[2]/span[8]/span")
c= driver.find_element_by_xpath("(//div/a/span[text()='Watches'])[1]")

action = ActionChains(driver).move_to_element(a).move_to_element(b).move_to_element(c).click(c).perform()
time.sleep(5)
driver.find_element_by_xpath("//div/p/a[text()='Fastrack']").click()


import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")

driver = webdriver.Edge(executable_path="F:\Drivers\MicrosoftWebDriver.exe")

#driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")

#driver = webdriver.PhantomJS(executable_path="C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

driver.get("http://opensource.demo.orangehrmlive.com/login")
#driver.maximize_window()
print driver.title
time.sleep(5)
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin")
driver.find_element_by_id("btnLogin").click()
time.sleep(5)
pim = driver.find_element_by_xpath("//a/b[text()='PIM']")
reports = driver.find_element_by_xpath("//a[text()='Reports']")
#driver.find_element_by_id("id_")

actions = ActionChains(driver).move_to_element(pim).move_to_element(reports).click(reports).perform()

print driver.title
time.sleep(5)
driver.close()



import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By 
#from selenium.webdriver.common.keys import Keys



chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notificationss")
#chrome_options.add_experimental_option("profile.default_content_setting_values.notifications", 2)#0-default,1-Allow,2-Block

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.amazon.in/")
time.sleep(5)

#driver.find_element_by_class_name("name").send_keys(Keys.UP)

print driver.title
pim = driver.find_element_by_xpath("//a[@id='nav-link-yourAccount']")
reports = driver.find_element_by_xpath("//div[@id='nav-flyout-ya-signin']/a/span")
actions = ActionChains(driver).move_to_element(pim).move_to_element(reports).click(reports).perform()
time.sleep(5)
driver.find_element_by_id("ap_email").send_keys("gvkreddy71@gmail.com")
driver.find_element_by_xpath("//span/input[@id='continue']").click()
driver.find_element_by_id("ap_password").send_keys("amazon271")
driver.find_element_by_id("signInSubmit").click()
print driver.title
driver.get_screenshot_as_file("amazon123.png")

cat = Select(driver.find_element_by_xpath("//select[@id='searchDropdownBox']"))
cat.select_by_visible_text("Books")

opt = cat.options
for i in opt:
    print i.get_attribute("innerHTML")
    
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("chetan bhagat")
driver.find_element_by_xpath("//input[@class='nav-input' and @value='Go']").click()
print driver.title

time.sleep(5)
driver.close()
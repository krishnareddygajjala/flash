
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.page_Actions import hover_over_element


#driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver = webdriver.Edge(executable_path="F:\Drivers\MicrosoftWebDriver.exe")
driver.get("https://www.ajio.com/shop/men")
#driver.maximize_window()
print driver.title
time.sleep(5)

men = driver.find_element_by_xpath("//a[@title='MEN']")

actions = ActionChains(driver).move_to_element(men).perform()
time.sleep(5)
try:
    backpacks = driver.find_element_by_xpath("//div[@class='items']/a[@title='Jeans']")

    actions = ActionChains(driver).move_to_element(men).move_to_element(backpacks).click(backpacks).perform()
except Exception as e:
    print e
print driver.title
time.sleep(10)
driver.close()

#//div[@class='items']/a[@title='Jeans']
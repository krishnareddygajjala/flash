
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://www.parker.com/portal/site/PARKER/menuitem.bc659799d3cf5c6315731910237ad1ca/?vgnextoid=ad6acab60275e210VgnVCM10000048021dacRCRD&vgnextfmt=EN")
ele = driver.find_element_by_xpath(".//div/input[@id='searchHomeValue']")
time.sleep(10)
print ele.is_displayed()
print ele.is_enabled()
ele.send_keys("krishna")
driver.find_element_by_xpath("//button[text()='Search']").click()
driver.get_screenshot_as_file("krishna.png")
time.sleep(5)
driver.close()
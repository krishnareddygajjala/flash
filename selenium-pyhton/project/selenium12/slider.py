
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as kys
from selenium.webdriver.common.action_chains import ActionChains
from pyrobot.pyrobot import Robot,Keys


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://www.globalsqa.com/demo-site/sliders/#Steps")
driver.maximize_window()
time.sleep(10)

ele= driver.find_element(By.XPATH,".//*[@id='menu-item-1513']/a")
point = ele.location
print point
xcord = point.get("x")
ycord = point.get("y")
print xcord,ycord

robot = Robot()
actions = ActionChains(driver)
# source = driver.find_element_by_xpath("//div[@id='slider']/span[@style='left: 20%;']")
# target = driver.find_element_by_xpath("//div[@id='slider']/span[@style='left: 60%;']")
# actions.drag_and_drop(source, target)
actions.move_to_element_with_offset(ele, int(xcord),int(ycord)).click(ele).perform()
actions.key_down(kys.CONTROL)



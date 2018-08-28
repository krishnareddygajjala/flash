import time
from pyrobot.pyrobot import Robot,Keys
from selenium import webdriver

robot = Robot()

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://encodable.com/uploaddemo/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='uploadname1']").click()      #.send_keys("C:\Users\Ram\Desktop\Tvamasmin-Telugu.jpg")

robot.add_to_clipboard("C:\Users\Ram\Desktop\Tvamasmin-Telugu.jpg")
print robot.get_clipboard_data()
time.sleep(5)
robot.paste()
print robot.paste()
robot.key_press(Keys.left_control)
robot.key_press(Keys.v)
robot.key_release(Keys.v)
robot.key_release(Keys.left_control)
time.sleep(5)
#robot.paste()
#robot.ctrl_press("v")
print robot.get_clipboard_data()
robot.key_press(Keys.enter)
robot.key_release(Keys.enter)
time.sleep(10)
print driver.title
driver.quit()

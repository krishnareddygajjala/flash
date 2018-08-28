import time
from pyrobot.pyrobot import Robot,Keys
from selenium import webdriver

robot = Robot()

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.phptravels.net/login")
driver.maximize_window()
time.sleep(5)

window_before = driver.window_handles[0]
print "window_before"+window_before

driver.get_screenshot_as_file("demo12345.png")
print driver.title
driver.find_element_by_xpath("//input[@name='username']").send_keys("user@phptravels.com")
driver.find_element_by_xpath("//input[@name='password']").send_keys("demouser")
try:
    driver.find_element_by_xpath("//button[@type='submit' and text()='Login']").click()
except Exception as e:
    driver.get_screenshot_as_file("failtest000.png")
    print e
    
time.sleep(5)
driver.find_element_by_xpath("(//a[text()='Invoice'])[1]").click()
time.sleep(5)
robot.key_press(Keys.down_arrow)
robot.key_press(Keys.down_arrow)
robot.key_press(Keys.down_arrow)
robot.key_press(Keys.down_arrow)
robot.key_press(Keys.down_arrow)
robot.key_press(Keys.down_arrow)
robot.key_press(Keys.down_arrow)
#driver.execute_script("window.scrollTo(0, 720)") 
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
print "window_after"+window_after

time.sleep(10)
try:
    driver.find_element_by_xpath(".//*[@id='downloadInvoice']").click()
except Exception as e:
    print e
    
print driver.title
time.sleep(5)
robot.key_press(Keys.enter)
robot.key_release(Keys.enter)
time.sleep(10)
driver.quit()
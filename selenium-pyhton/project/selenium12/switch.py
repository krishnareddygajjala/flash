
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.redbus.in/")
driver.maximize_window()
print driver.title

username = "krrishna9848@gmail.com"
password = "password@9848"
driver.find_element_by_id("signin-block").click()
driver.find_element_by_id("signInLink").click()
time.sleep(5)
try:
    driver.switch_to.frame(driver.find_element_by_xpath("//div[@style='height: 417px; width: 710px; top: -208.5px; left: -355px;']"))
    time.sleep(10)
    driver.find_element_by_xpath("//a[@class='signin-screen' and text()='sign in']").click()
    driver.find_element_by_id("email-mobile").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(5)

except Exception as e:
    print "error",e
    
driver.close()
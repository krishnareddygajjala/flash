from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://ph.parker.com/in/en/CreateAccount?myAcctMain=1&new=Y")
driver.find_element_by_name("firstName").send_keys("krishna")
driver.find_element_by_name("lastName").send_keys("reddy")
driver.find_element_by_name("logonId").send_keys("reddy")
driver.find_element_by_name("email1").send_keys("reddy")
driver.find_element_by_name("logonPassword").send_keys("reddy")
driver.find_element_by_name("logonPasswordVerify").send_keys("reddy")
try:
    driver.find_element_by_xpath("//button[@aria-expanded='false']").click()
    all_options =driver.find_elements_by_xpath("//li[@role='presentation']")
    for option in all_options:
        print option.get_attribute("innerHTML")
except NoSuchElementException as err:
    print err.message
finally:
    pass
    

driver.find_element_by_xpath("//input[@name='challengeAnswer']").send_keys("answer")
time.sleep(10)
try:
    cap = driver.find_element_by_xpath("//div[@class= 'recaptcha-checkbox-checkmark']").click()
except NoSuchElementException as err:
    print err.message
    


print driver.title
time.sleep(10)
driver.close()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://demo.guru99.com/test/ajax.html")
driver.fullscreen_window()
wait = WebDriverWait(driver,10)
try:
    ele = wait.until(EC.element_to_be_clickable((By.ID,'yes'))).click()
    print "element is ready to clickable"
    driver.find_element_by_xpath("//input[@id='buttoncheck']").click()
    ele1 = wait.until(EC.presence_of_element_located((By.XPATH,"//p[@class='radiobutton']")))
    print ele1.get_attribute("innerHTML")
finally:
    time.sleep(5) 
    print driver.name
    driver.close()
    


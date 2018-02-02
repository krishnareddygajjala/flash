from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="F:\selenium required software\selenium drivers\chromedriver.exe")
driver.get("https://www.flipkart.com/")
driver.find_element_by_class_name("_2zrpKA").send_keys("rajureddy.gontika@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("flipkart271")
driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
driver.implicitly_wait(5)
driver.get_screenshot_as_file("flipkart.png")
#hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[@class='_1QZ6fC']/span")).move_to_element(driver.find_element_by_xpath("//a[@class='_3ZgIXy' and @title='Mi']")).click().perform()
time.sleep(30)
#driver.find_element_by_xpath("//div[@class='_3wU53n' and @innerHTML='Mi A1 (Black, 64 GB)']").click()
print driver.title
driver.quit()
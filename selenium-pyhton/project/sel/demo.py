from selenium import webdriver
import time 
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="F:\selenium required software\selenium drivers\chromedriver.exe")
driver.get("https://www.flipkart.com/?affid=evevisser&affExtParam1=2&affExtParam2=AAd9TFoCAAAAqpIAAElOFwAMALOWccMA")
#driver.implicitly_wait(10)
driver.find_element_by_xpath("html/body/div[2]/div/div/button").click()
ele = driver.find_element_by_class_name("//a[@class='sYph0c' and @title='Men']")
signin = driver.find_element_by_xpath(".//*[@id='container']/div/header/div[3]/div/ul/li[3]/ul/li/ul/li[1]/ul/li[3]/a/span") 
actions = ActionChains(driver)
actions.move_to_element(ele).move_to_element(signin).perform()
actions.click(signin)


time.sleep(3)
driver.close()




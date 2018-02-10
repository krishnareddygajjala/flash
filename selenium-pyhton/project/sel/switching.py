from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="F:\selenium required software\selenium drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="F:\selenium required software\selenium drivers\geckodriver.exe")
driver.get("https://www.naukri.com/")

driver.implicitly_wait(10)

driver.window_handles
home = driver.title
print home



#ele = driver.find_element_by_xpath("//div[@class='mTxt' and text()='Companies']")
#ele1 = driver.find_element_by_xpath("//a[@title='Interview Questions']")
#mouseactions = ActionChains(driver).move_to_element(ele).move_to_element(ele1).click(ele1).perform()

#driver.find_element_by_xpath(".//*[@id='gbw']/div/div/div[1]/div[1]/a").click()
#driver.find_element_by_xpath("//a[text()='Help']").click()
#driver.find_element_by_xpath("//a[text()='Privacy']").click()
#driver.find_element_by_xpath("//a[text()='Terms']").click()
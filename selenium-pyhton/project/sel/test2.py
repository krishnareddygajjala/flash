from selenium import webdriver
#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.facebook.com/")

element = driver.find_element_by_id("month")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("innerHTML"))
    option.click()
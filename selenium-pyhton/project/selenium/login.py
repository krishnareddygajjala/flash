
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")

driver.get("http://www.gcrit.com/build3/login.php")
try:
    driver.find_element_by_name("email_address").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin@123")
    driver.find_element_by_id("tdb5").click()
finally:
    print "invalid credentials"
    errmsg = driver.find_element_by_xpath("//td[@class='messageStackError']").get_attribute("innerHTML")
    print errmsg
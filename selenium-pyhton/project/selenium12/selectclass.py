
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
#driver = webdriver.PhantomJS(executable_path="C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("http://www.gcrit.com/build3/create_account.php")
driver.maximize_window()
country = Select(driver.find_element_by_name("country"))
country.select_by_value("99")#india
time.sleep(5)
#country.select_by_index(index)
country.select_by_visible_text("Indonesia")

time.sleep(5)

driver.close()

#select = driver.find_element_by_xpath("//select")
#all_options = select.find_elements_by_tag_name("option")
#for option in all_options:
#    print "Value is: %s" % option.get_attribute("value")
#    option.click()
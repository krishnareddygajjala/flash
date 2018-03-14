import sys
import traceback
from selenium import webdriver
import time 


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("http://www.gcrit.com/build3/create_account.php")
time.sleep(10)
try:
    driver.find_element_by_xpath("//select[@name='countr']")
#all_options = country.find_elements_by_tag_name("options")
#for i in all_options:
    #print "country name is : %s" %i.get_attribute("innerHTML")
except Exception as e:
    print e
    print traceback.format_exc(sys.exc_info())
    
    
driver.close()

from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
#driver = webdriver.PhantomJS(executable_path="C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("http://www.gcrit.com/build3/create_account.php")
driver.maximize_window()
country = driver.find_element_by_name("country")
all_options = country.find_elements_by_tag_name("options")
for i in all_options:
    print "country name is : %s" %i.get_attribute("innerHTML")
    
    
    
    
driver.close()
    
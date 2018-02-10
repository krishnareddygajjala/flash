
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.google.co.in/")
driver.maximize_window()
links = driver.find_elements_by_tag_name("a")
print len(links)
for i in links:
    print i.get_attribute("href")
    




driver.close()
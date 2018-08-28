import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.redbus.in/")
#driver.maximize_window()
driver.fullscreen_window()
print driver.title
print driver.name
a = driver.execute_script("return document.title;")
print a
b = driver.execute_script("return document.getElementById('page_main_header').getAttribute('class');")
print b
# c = driver.execute_script("return document.frames.length;")
# print c
driver.execute_script("window.scrollBy(0,150);")
driver.execute_script("alert('hello world');")

time.sleep(5)
driver.close()
driver.pa
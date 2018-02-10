
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.get_screenshot_as_file("google.png")




driver.close()
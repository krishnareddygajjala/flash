from selenium import webdriver

 
driver = webdriver.PhantomJS(executable_path="C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get('https://google.co.in/')
 
html = driver.title
print(html)
driver.close()
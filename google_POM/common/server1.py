from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selenium_grid_url = "http://localhost:4444/wd/hub"

# Create a desired capabilities object as a starting point.
capabilities = DesiredCapabilities.EDGE#.copy()
#capabilities['platform'] = "WINDOWS"
#capabilities['version'] = "10"

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                                  command_executor=selenium_grid_url)
driver.get("https://www.facebook.com")
print driver.title
driver.close()


#Note: Always use '.copy()' on the DesiredCapabilities object to avoid the side effects of altering the Global class instance.
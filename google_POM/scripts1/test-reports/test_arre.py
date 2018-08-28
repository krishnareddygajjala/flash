
import time
from selenium import webdriver
from common.page_Actions import hover_over_element


#driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
driver = webdriver.Edge(executable_path="F:\Drivers\MicrosoftWebDriver.exe")
driver.get("http://www.arre.co.in/")
#driver.maximize_window()
print driver.title
time.sleep(10)

hover_over_element(driver, "html/body/header/div[1]/nav/ul/li[1]/a")
time.sleep(10)


dirc = os.getcwd()
print dirc
outfile = open(dirc + "\SeleniumPythonTestSummary.html", "w")
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile,title='Test Report')#, description='Acceptance Tests'
home_page_test = unittest.TestLoader().loadTestsFromTestCase(homepagetest)
test_suite = unittest.TestSuite([home_page_test])
runner.run(test_suite)
driver.close()




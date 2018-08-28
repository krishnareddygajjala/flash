
#import HtmlTestRunner
import HTMLTestRunner
import unittest, time, os
from selenium import webdriver
from common.page_Actions import hover_over_element

class testclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")

    def test_Method(self):
        driver = self.driver
        driver.get("http://www.arre.co.in/")
        driver.maximize_window()
        print driver.title
        time.sleep(5)

        hover_over_element(driver, "html/body/header/div[1]/nav/ul/li[1]/a")
        time.sleep(5)
        dirc = os.getcwd()
        print dirc
        dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
        print dateTimeStamp
        
       
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    HTMLTestRunner.main(HTMLTestRunner.HTMLTestRunner(stream='TestReport',title='My unit test',description='This demonstrates the report output by HTMLTestRunner.'))


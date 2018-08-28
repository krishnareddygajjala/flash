
import sys
import time
import unittest2 as unittest
import HtmlTestRunner
from TestBase.EnvironmentSetup import EnvironmentSetup


class dummy(EnvironmentSetup):
    
    def testca(self):
        driver = self.driver
        
        self.driver.get("http://www.gcrit.com/build3/index.php")
        self.driver.set_page_load_timeout(20)
        print driver.title
        #self.driver.get_screenshot_as_png("dummy")    
        
    
if  __name__ == '__main__':
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    file_name = "TestReport" + "_" + dateTimeStamp + ".html"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(stream = sys.stderr, output=file_name, descriptions="sample test"))

import os
import sys
import time
import traceback
#import xmlrunner
import HtmlTestRunner
import unittest2 as unittest
from TestBase.EnvironmentSetup import EnvironmentSetup
from pageObject.pages.homepage import Home
from pageObject.pages.createAccountpage import createAccount



class homepagetest(EnvironmentSetup):
    
    def testca(self):
        driver = self.driver
        
        self.driver.get("http://www.gcrit.com/build3/index.php")
        self.driver.set_page_load_timeout(20)
        
        home = Home(driver)
        time.sleep(5)
        home.getcreateAccount().click()
        time.sleep(5)
        
        ca = createAccount(driver)
        time.sleep(3)
        try:
            ca.getradiobuttonmale().click()
            ca.getfirstname("krishna")
            ca.getlastname("reddy")
            ca.getdob("01/01/1990")
            ca.getcompanyname("graylocus")
            ca.getcity("bangalore")
            ca.getemail("krishna@gmail.com")
            ca.getstreet("BTM 1st stage")
            ca.getpost_code(560029)
            ca.getstate("karnataka")
            ca.getsuburb("btm")
            ca.getpassword("admin123")
            ca.getpassword_confirmation("admin")
            
            ca.select(ca.getcountry(), "India")
            
            ca.gettelephone(123456789)
            ca.getfax(321654987)
            ca.getnewsletter().click()
            #ca.getcontinue1().click()
            
            time.sleep(5)
            print driver.title
            #print ca.geterrmsg().get_attribute("innerHTML")
            
            
            
        except Exception as e:
            print e
            print traceback.format_exc(sys.exc_info())


if  __name__ == '__main__':
    dirc = os.getcwd()
    print dirc
    file_name = "SeleniumPythonTestSummary.html"
    
    suite = unittest.TestLoader().loadTestsFromTestCase(homepagetest)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(stream=sys.stderr, output=file_name, descriptions='Acceptance Tests', report_title="dummy html report"))
        
        
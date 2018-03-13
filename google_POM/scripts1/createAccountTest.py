
import time
import unittest
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
            #ca.getdob("09/10/1992")
            ca.getcompanyname("graylocus")
            ca.getcity("bangalore")
            ca.getemail("krrishna9848@gmail.com")
            ca.getstreet("BTM")
            
            
            
            time.sleep(5)
            print driver.title
        except Exception as e:
            print e





if  __name__ == '__main__':
    unittest.main()
        
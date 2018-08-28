
import unittest2 as unittest
from TestBase.EnvironmentSetup import EnvironmentSetup


class dummy(EnvironmentSetup):
    def testca(self):
        driver = self.driver
        
        self.driver.get("http://www.gcrit.com/build3/index.php")
        self.driver.set_page_load_timeout(20)
    
    

    
    
    
    
    
if  __name__ == '__main__':
    unittest.main()
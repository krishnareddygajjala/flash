
import unittest2 as unittest
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):
    
    def setUp(self):
        path = 'C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path)
        print "test environment started"
        print "*********************************"
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()

    def tearDown(self):
        print "*********************************"
        print "test environment destroyed"
        self.driver.close()
        self.driver.quit()
        
        
        
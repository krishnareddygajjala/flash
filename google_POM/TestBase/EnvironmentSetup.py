
import unittest
#simport datetime
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Users\Ram\PycharmProjects\untitled2\divers\chromedriver.exe")
        print "*********************************"
        print "test environment started"
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()

    def tearDown(self):
        print "*********************************"
        print "test environment destroyed"
        self.driver.close()
        self.driver.quit()
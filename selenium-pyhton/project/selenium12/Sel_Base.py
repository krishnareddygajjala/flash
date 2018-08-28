import unittest2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Base(unittest2.TestCase):
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
        
    def hover_onthe_element(self,driver, selector, by=By.CSS_SELECTOR):
        """
        Fires the hover event for the specified element by the given selector.
        @Params
        driver - the webdriver object (required)
        selector - the locator (css selector) that is used (required)
        by - the method to search for the locator (Default: By.CSS_SELECTOR)
        """
        element = driver.find_element(by=by, value=selector)
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        
        
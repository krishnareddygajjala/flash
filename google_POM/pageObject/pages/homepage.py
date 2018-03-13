
__author__ = 'krishna'

from pageObject.Locators import Locators

class Home(object):
    
    def __init__(self,driver):
        self.driver = driver

        #home page locators defining
        self.login = driver.find_element_by_xpath(Locators.login)
        self.createAccount = driver.find_element_by_xpath(Locators.createAccount)

    def getLogin(self):
        return self.login
    def getcreateAccount(self):
        return self.createAccount
        
        
        
    

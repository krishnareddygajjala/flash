
from pageObject.Locators import Locators


class createAccount(object):
    
    def __init__(self,driver):
        self.driver = driver
        
#create account page

        self.male_radio = driver.find_element_by_xpath(Locators.male_radio)
        self.female_radio = driver.find_element_by_xpath(Locators.female_radio)
        self.first_name = driver.find_element_by_xpath(Locators.first_name)
        self.last_name = driver.find_element_by_xpath(Locators.last_name)
        self.dob = driver.find_element_by_xpath(Locators.dob)
        self.company_name = driver.find_element_by_xpath(Locators.company_name)
        self.street = driver.find_element_by_xpath(Locators.street)
        self.email = driver.find_element_by_xpath(Locators.email)
        self.suburb = driver.find_element_by_xpath(Locators.suburb)
        self.post_code = driver.find_element_by_xpath(Locators.post_code)
        self.city = driver.find_element_by_xpath(Locators.city)
        self.state = driver.find_element_by_xpath(Locators.state) 
    
    def getradiobuttonmale(self):
        return self.male_radio
    def getradiobuttonfemale(self):
        return self.female_radio
    def getfirstname(self,fname):
        self.first_name.clear()
        self.first_name.send_keys(fname)
    def getlastname(self,lname):
        self.last_name.clear()
        self.last_name.send_keys(lname)
    def getdob(self,dob):
        self.dob.clear()
        self.dob.send_keys(dob)
    def getcompanyname(self,company_name):
        self.company_name.clear()
        self.company_name.send_keys(company_name)
    def getstreet(self,street):
        self.street.clear()
        self.street.send_keys(street)
    def getemail(self,email):
        self.email.clear()
        self.email.send_keys(email)
    def getsuburb(self,suburb):
        self.suburb.clear()
        self.suburb.send_keys(suburb)
    def getpost_code(self,post_code):
        self.post_code.clear()
        self.post_code.send_keys(post_code)
    def getcity(self,city):
        self.city.clear()
        self.city.send_keys(city)
    def getstate(self,state):
        self.state.clear()
        self.state.send_keys(state)
        
        
        
        
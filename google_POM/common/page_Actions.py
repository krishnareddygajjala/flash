

#from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def hover_over_element(driver, selector, by=By.XPATH):
    """
    Fires the hover event for the specified element by the given selector.
    @Params
    driver - the webdriver object (required)
    selector - the locator (css selector) that is used (required)
    by - the method to search for the locator (Default: By.XPATH)
    """
    element = driver.find_element(by=by, value=selector)   
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
    
    








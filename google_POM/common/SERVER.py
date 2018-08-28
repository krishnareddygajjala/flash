
import unittest
#from time import sleep
from selenium import webdriver


class TestParallel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            #desired_capabilities=webdriver.DesiredCapabilities.OPERA,
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                "browserName": "opera",}
            )
        #self.driver.implicitly_wait(30)
        self.driver.maximize_window()

#     def test_four(self):
#         driver = self.driver
#         driver.get("https://www.google.org")

    def test_five(self):
        driver = self.driver
        driver.get("https://www.facebook.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=3)

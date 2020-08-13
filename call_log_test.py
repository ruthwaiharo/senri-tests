import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class call_log_test(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '5LX9K18C12906909'
        self.dc['appPackage'] = 'com.afri_inc.senri'
        self.dc['appActivity'] = '.activity.HomeActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='Call Log']").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="menuButton" and (./preceding-sibling::* | ./following-sibling::*)[@text="12 Aug, 21:05"]]')))
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='menuButton' and (./preceding-sibling::* | ./following-sibling::*)[@text='12 Aug, 21:05']]").click()
        assert self.driver.find_element_by_xpath("xpath=//*[@id='menuButton' and (./preceding-sibling::* | ./following-sibling::*))").is_displayed() is True
#this is a new asertion


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

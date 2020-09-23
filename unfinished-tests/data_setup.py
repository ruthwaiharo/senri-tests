import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class data_setup(unittest.TestCase):
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

    def create_customer(self, customer_name):
        self.driver.find_element_by_xpath("xpath=//*[@text='NEW RECORD']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='sd_main_fab']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='name_path']").type(customer_name)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='Coin Ball']")))
        self.driver.find_element_by_xpath("xpath=//*[@text='Coin Ball']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='sd_main_fab']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='sd_main_fab']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='CREATE CUSTOMER']").click()


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

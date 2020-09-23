import unittest
from tests import data_setup as data_setup
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class senri_test(unittest.TestCase):
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

    def test_customer_can_check_out(self):
        customerName = "Customer 3"
        data_setup.create_customer(customerName)
        self.driver.find_element_by_xpath("xpath=//*[@text='NEW RECORD']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text={customerName}]")))
        self.driver.find_element_by_xpath("xpath=//*[@text='{customerName}']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='sd_main_fab']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='sd_main_fab']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='CHECKIN']").click()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='CHECK OUT']").is_displayed() is True

        # self.driver.find_element_by_xpath("xpath=//*[@text='CHECK OUT']").click()
        # assert self.driver.find_element_by_xpath("xpath=//*[@text='WRITE VISIT REPORT LATER']").is_displayed() is True

    def test_customer_can_make_sale(self):
        customerName = "Customer 3"
        data_setup.create_customer(customerName)
        data_setup.check_in_customer(customerName)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

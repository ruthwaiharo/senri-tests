import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
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
        self.driver.find_element_by_accessibility_id('Open navigation drawer').click()
        assert self.driver.find_element_by_id('accountName').is_displayed()
        assert self.driver.find_element_by_id('companyName').is_displayed()
        assert self.driver.find_element_by_id('captionPastRecord').is_displayed()
        assert self.driver.find_element_by_id('pastRecordSales').is_displayed()
        assert self.driver.find_element_by_id('pastRecordSalesQuantities').is_displayed()
        assert self.driver.find_element_by_id('pastRecordDeliveries').is_displayed()
        assert self.driver.find_element_by_id('pastRecordPayments').is_displayed()
        assert self.driver.find_element_by_id('pastRecordVisitReports').is_displayed()
        assert self.driver.find_element_by_id('captionOther').is_displayed()
        assert self.driver.find_element_by_id('otherSubInventory').is_displayed()
        assert self.driver.find_element_by_id('otherShowRefreshDetail').is_displayed()
        assert self.driver.find_element_by_id('otherLastUpdateTime').is_displayed()
        assert self.driver.find_element_by_id('otherDownloadAndRefresh').is_displayed()
        self.driver.swipe('[0, 1286][560, 1356],[32,1259][197,1340]')
        assert self.driver.find_element_by_id('otherAbout').is_displayed()
        assert self.driver.find_element_by_id('otherLogOut').is_displayed()
        assert self.driver.find_element_by_id('version').is_displayed()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

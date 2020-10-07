import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class HomeScreenTest(unittest.TestCase):
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

    def testHomeScreen(self):
        # assert self.driver.find_element_by_accessibility_id('Open navigation drawer').is_displayed()
        # assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('refreshMessage').is_displayed()
        assert self.driver.find_element_by_id('todayActivityCaption').is_displayed()
        assert self.driver.find_element_by_id('callLogCaption').is_displayed()
        assert self.driver.find_element_by_id('callLogNavigationArrow').is_displayed()
        assert self.driver.find_element_by_id('todayActivitySalesCaption').is_displayed()
        assert self.driver.find_element_by_id('todayActivitySalesUnit').is_displayed()
        assert self.driver.find_element_by_id('todayActivitySalesArrow').is_displayed()
        assert self.driver.find_element_by_id('todayActivityVisitCaption').is_displayed()
        assert self.driver.find_element_by_id('todayActivityVisitCount').is_displayed()
        assert self.driver.find_element_by_id('yesterdayVisitCaption').is_displayed()
        assert self.driver.find_element_by_id('yesterdayVisitCount').is_displayed()
        assert self.driver.find_element_by_id('monthlyCaption').is_displayed()
        assert self.driver.find_element_by_id('monthlySalesCaption').is_displayed()
        assert self.driver.find_element_by_id('monthlySalesUnit').is_displayed()
        assert self.driver.find_element_by_id('monthlySalesArrow').is_displayed()
        assert self.driver.find_element_by_id('spacer').is_displayed()
        assert self.driver.find_element_by_id('tab_icon').is_displayed()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

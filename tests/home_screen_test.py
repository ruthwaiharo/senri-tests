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
        assert self.driver.find_element_by_accessibility_id('Open navigation drawer').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('refreshMessage').is_displayed()
        assert self.driver.find_element_by_id('todayActivityCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('callLogCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('callLogNavigationArrow').click().is_displayed() is True
        assert self.driver.find_element_by_id('todayActivitySalesCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('todayActivitySalesUnit').click().is_displayed() is True
        assert self.driver.find_element_by_id('todayActivitySalesArrow').click().is_displayed() is True
        assert self.driver.find_element_by_id('todayActivityVisitCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('todayActivityVisitCount').click().is_displayed() is True
        assert self.driver.find_element_by_id('yesterdayVisitCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('yesterdayVisitCount').click().is_displayed() is True
        assert self.driver.find_element_by_id('monthlyCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('monthlySalesCaption').click().is_displayed() is True
        assert self.driver.find_element_by_id('monthlySalesUnit').click().is_displayed() is True
        assert self.driver.find_element_by_id('monthlySalesPrimaryCustomerArrow').click().is_displayed() is True
        assert self.driver.find_element_by_id('spacer').click().is_displayed() is True
        assert self.driver.find_element_by_id('tab_icon').click().is_displayed() is True

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

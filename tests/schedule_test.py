import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class ScheduleTest(unittest.TestCase):
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

    def testSchedule(self):
        assert self.driver.find_element_by_accessibility_id('Open navigation drawer').click().is_displayed() is True
        assert self.driver.find_element_by_id('titleOnToolbar').click().is_displayed() is True
        assert self.driver.find_element_by_id('actionButton').click().is_displayed() is True
        assert self.driver.find_element_by_id('scroll_to_today').click().is_displayed() is True
        assert self.driver.find_element_by_accessibility_id('Display Removed Plan').click().is_displayed() is True
        assert self.driver.find_element_by_id('More options').click().is_displayed() is True
        assert self.driver.find_element_by_id('downloadImageView').click().is_displayed() is True
        assert self.driver.find_element_by_id('announceText').click().is_displayed() is True
        assert self.driver.find_element_by_id('displayDate').click().is_displayed() is True
        assert self.driver.find_element_by_id('menuButton').click().is_displayed() is True
        assert self.driver.find_element_by_id('').click().is_displayed() is True
        assert self.driver.find_element_by_id('displayCustomerName').click().is_displayed() is True
        assert self.driver.find_element_by_id('navigationArrow').click().is_displayed() is True
        assert self.driver.find_element_by_id('listView').click().is_displayed() is True

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

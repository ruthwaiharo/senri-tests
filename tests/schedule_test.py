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
        self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='SCHEDULE']/android.view.ViewGroup").click()
        assert self.driver.find_element_by_accessibility_id('Open navigation drawer').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('actionButton').is_displayed()
        assert self.driver.find_element_by_id('scroll_to_today').is_displayed()
        assert self.driver.find_element_by_accessibility_id('Display Removed Plan').is_displayed()
        assert self.driver.find_element_by_id('More options').is_displayed()
        assert self.driver.find_element_by_id('downloadImageView').is_displayed()
        assert self.driver.find_element_by_id('announceText').is_displayed()
        assert self.driver.find_element_by_id('displayDate').is_displayed()
        assert self.driver.find_element_by_id('menuButton').is_displayed()
        assert self.driver.find_element_by_id('').is_displayed()
        assert self.driver.find_element_by_id('displayCustomerName').is_displayed()
        assert self.driver.find_element_by_id('navigationArrow').is_displayed()
        assert self.driver.find_element_by_id('listView').is_displayed()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class NewRecordTest(unittest.TestCase):
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

    def testNewRecord(self):
        self.driver.find_element_by_id('spacer').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "filterBy")))
        assert self.driver.find_element_by_accessibility_id('Navigate up').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('action_search').is_displayed()
        assert self.driver.find_element_by_id('sortedBy').is_displayed()
        assert self.driver.find_element_by_id('sortedByIcon').is_displayed()
        assert self.driver.find_element_by_id('filterIcon').is_displayed()
        assert self.driver.find_element_by_id('filterBy').is_displayed()
        assert self.driver.find_element_by_id('index').is_displayed()
        assert self.driver.find_element_by_id('customerName').is_displayed()
        assert self.driver.find_element_by_id('subInfo').is_displayed()
        assert self.driver.find_element_by_id('customerPriority').is_displayed()
        assert self.driver.find_element_by_id('fabButton').is_displayed()

    def testFilterOption(self):
        self.driver.find_element_by_id('spacer').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "filterBy")))
        self.driver.find_element_by_id('filterBy').click()
        assert self.driver.find_element_by_id('alertTitle').is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='All']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Primary Customer']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Secondary Customer']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='CANCEL']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='OK']").is_displayed()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

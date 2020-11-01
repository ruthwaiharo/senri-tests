import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class ExistingCustomerTest(unittest.TestCase):
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

    def testCustomerDetail(self):
        self.driver.find_element_by_id('spacer').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID,'customerName')))
        self.driver.find_element_by_id('customerName').click()
        assert self.driver.find_element_by_accessibility_id('Navigate up').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('action_edit').is_displayed()
        assert self.driver.find_element_by_id('customerName').is_displayed()
        assert self.driver.find_element_by_id('directionIcon').is_displayed()
        assert self.driver.find_element_by_id('directionText').is_displayed()
        assert self.driver.find_element_by_id('callDisabledIcon').is_displayed()
        assert self.driver.find_element_by_id('callText').is_displayed()
        assert self.driver.find_element_by_id('addressIcon').is_displayed()
        assert self.driver.find_element_by_id('addressCaption').is_displayed()
        assert self.driver.find_element_by_id('addressValue').is_displayed()
        assert self.driver.find_element_by_id('addressSection').is_displayed()
        assert self.driver.find_element_by_id('pastSalesIcon').is_displayed()
        assert self.driver.find_element_by_id('pastSalesCaption').is_displayed()
        assert self.driver.find_element_by_id('pastSalesValue').is_displayed()
        assert self.driver.find_element_by_id('pastSalesNavigationArrow').is_displayed()
        assert self.driver.find_element_by_id('lastVisitIcon').is_displayed()
        assert self.driver.find_element_by_id('lastVisitCaption').is_displayed()
        assert self.driver.find_element_by_id('lastVisitValue').is_displayed()
        assert self.driver.find_element_by_id('lastVisitNavigationArrow').is_displayed()
        assert self.driver.find_element_by_id('sd_main_fab').is_displayed()

    def testBackButtonPrompt(self):
        self.driver.find_element_by_id('spacer').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID,'customerName')))
        self.driver.find_element_by_id('customerName').click()
        self.driver.find_element_by_id('action_edit').click()
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        assert self.driver.find_element_by_id('alertTitle').is_displayed()
        assert self.driver.find_element_by_id('message').is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='DISCARD']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").is_displayed()

    def testEditCustomerDetail(self):
        self.driver.find_element_by_id('spacer').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID,'customerName')))
        self.driver.find_element_by_id('customerName').click()
        self.driver.find_element_by_id('action_edit').click()
        assert self.driver.find_element_by_accessibility_id('Navigate up').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('customerGroupCaption').is_displayed()
        assert self.driver.find_element_by_id('inputName').is_displayed()
        assert self.driver.find_element_by_id('requiredOfName').is_displayed()
        assert self.driver.find_element_by_id('customerPriorityTitle').is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Primary Customer']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Secondary Customer']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Tier']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Customer Type']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Region']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Area']").is_displayed()
        self.driver.swipe(588, 925, 588, 65, 1123)
        assert self.driver.find_element_by_id('streetEditText').is_displayed()
        assert self.driver.find_element_by_id('telephoneEditText').is_displayed()
        assert self.driver.find_element_by_id('telephone2EditText').is_displayed()
        assert self.driver.find_element_by_id('inputLocation').is_displayed()
        assert self.driver.find_element_by_id('locationUpdateIcon').is_displayed()
        assert self.driver.find_element_by_id('locationUpdateText').is_displayed()
        assert self.driver.find_element_by_id('noteEditText').is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Person in Charge']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Email Address']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Contact Number']").is_displayed()
        assert self.driver.find_element_by_id('photoGroupCaption').is_displayed()
        assert self.driver.find_element_by_id('addPhotoText').is_displayed()
        assert self.driver.find_element_by_id('navigationButton').click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

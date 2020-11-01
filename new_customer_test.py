import unittest
from appium import webdriver
from selenium import webdriver

class NewCustomerTest(unittest.TestCase):
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

    def testReturnButtonPrompt(self):
        self.driver.find_element_by_id('spacer').click()
        self.driver.find_element_by_id('fabButton').click()
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        assert self.driver.find_element_by_id('alertTitle').is_displayed()
        assert self.driver.find_element_by_id('message').is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='DISCARD']").is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").is_displayed()

    def testAddNewCustomer(self):
        self.driver.find_element_by_id('spacer').click()
        self.driver.find_element_by_id('fabButton').click()
        assert self.driver.find_element_by_accessibility_id('Navigate up').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('customerGroupCaption').is_displayed()
        assert self.driver.find_element_by_xpath("xpath=//*[@text='Name']").is_displayed()
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

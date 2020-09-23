import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class CallLogTest(unittest.TestCase):
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

    def test_call_log_test_unknown_number(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='Call Log']").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="callLogCaption")'
        self.driver.find_element_by_xpath("xpath=//*[@id='callLogCaption']").click()
        assert self.driver.find_element_by_xpath("xpath=//*[@id='menuButton' and (./preceding-sibling::* | ./following-sibling::*)]").is_displayed() is True
# this is a new assertion
        formData = [user[account]: "grant2", user[password]: "grant2"....]
        userResponse = requests.post("http://senri.afri-inc.com/users", formData).send
        user = userResponse.body
        self.driver.find_element_by_id("loginUserName").enterText("grant3")
        self.driver.find_element_by_id("loginPassword").enterText("123456")
        self.driver.find_element_by_id("logic").click()
        self.driver.find_element_by_id("xpath=//*[@id='callLogCaption']").click()

        def test_call_log_test(self):
            formData = [user[account]: "grant2", user[password]: "grant2"....]
            userResponse = requests.post("http://senri.afri-inc.com/users", formData).send
            user = userResponse.body
            self.driver.find_element_by_id("loginUserName").enterText("grant3")
            self.driver.find_element_by_id("loginPassword").enterText("123456")
            self.driver.find_element_by_id("logic").click()
            self.driver.find_element_by_id("xpath=//*[@id='callLogCaption']").click()
            assert self.driver.find_element_by_xpath("xpath=//*[@id='titleOnToolbar']").click().is_displayed() is True


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

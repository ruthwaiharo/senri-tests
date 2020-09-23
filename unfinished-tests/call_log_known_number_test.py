class tests_call_log_known_number_test(unittest.TestCase):
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
        self.driver.find_element_by_xpath("xpath=//*[@text='Call Log']").click()
        # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="7eb66b82-5721-4248-aa55-2cefce499482"))
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="call-log-item"]]')))
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='menuButton' and (./preceding-sibling::* | ./following-sibling::*)[@text='13 Aug, 12:58']]").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@text="Add New Customer"]')))
        self.driver.find_element_by_xpath("xpath=//*[@text='Add New Customer']").click()
        self.driver.swipe(430, 818, 430, -778, 882)
        self.driver.swipe(430, 726, 430, -30, 923)
        self.driver.swipe(430, 894, 430, 1902, 1386)
        self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

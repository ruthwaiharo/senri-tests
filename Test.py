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
        self.driver.find_element_by_xpath("xpath=//*[@text='NEW RECORD']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@text='0.0km' and (./preceding-sibling::* | ./following-sibling::*)[@text='ABC']]')))
        self.driver.find_element_by_xpath(
            "xpath=//*[@text='0.0km' and (./preceding-sibling::* | ./following-sibling::*)[@text='ABC']]").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id='sd_main_fab']')))
        self.driver.find_element_by_xpath("xpath=//*[@id='sd_main_fab']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text='VISIT']')))
        self.driver.find_element_by_xpath("xpath=//*[@text='VISIT']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Sales']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text='Existing Cient']')))
        self.driver.find_element_by_xpath("xpath=//*[@text='Existing Cient']").click()
        self.driver.swipe(374, 798, 374, 42, 812)
        self.driver.swipe(374, 1134, 374, 1806, 1150)
        self.driver.swipe(370, 1160, 370, 1580, 830)
        self.driver.swipe(378, 890, 378, 302, 1678)
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.EditText']").send_keys('ASD')
        self.driver.swipe(262, 928, 262, 340, 1322)
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.EditText' and ./parent::*[./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='Q6.']]]]").send_keys(
            'Delivery')
        self.driver.swipe(342, 276, 342, -228, 734)
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.EditText' and ./parent::*[./parent::*[@id='freeTextArea' and (./preceding-sibling::* | ./following-sibling::*)[@text='Q7.']]]]").send_keys(
            'N/A')
        self.driver.swipe(372, 218, 372, 134, 605)
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.EditText' and ./parent::*[./parent::*[@id='freeTextArea' and (./preceding-sibling::* | ./following-sibling::*)[@text='Q8.']]]]").send_keys(
            'They are happy ')
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text='SUBMIT']')))
        self.driver.find_element_by_xpath("xpath=//*[@text='SUBMIT']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='SUBMIT']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

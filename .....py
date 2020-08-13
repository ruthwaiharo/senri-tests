def testUntitled(self):
    self.driver.find_element_by_xpath("xpath=//*[@text='NEW RECORD']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='fabButton']").click()
    self.driver.find_element_by_xpath(
        "xpath=//*[@class='android.widget.EditText' and ./parent::*[./parent::*[@id='inputName']]]").send_keys('qwe')
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@text='Primary Customer']')))
    self.driver.find_element_by_xpath("xpath=//*[@text='Primary Customer']").click()
    self.driver.swipe(328, 444, 328, -396, 1001)
    self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()

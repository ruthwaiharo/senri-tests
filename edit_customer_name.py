def testUntitled(self):
    self.driver.find_element_by_xpath("xpath=//*[@text='NEW RECORD']").click()
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id='mainContents']')))
    self.driver.find_element_by_xpath("xpath=//*[@id='mainContents']").click()
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id='action_edit']')))
    self.driver.find_element_by_xpath("xpath=//*[@id='action_edit']").click()
    self.driver.find_element_by_xpath(
        "xpath=//*[@class='android.widget.EditText' and ./parent::*[./parent::*[@id='inputName']]]").click()
    self.driver.execute_script("seetest:client.deviceAction(\"BKSP\")")
    self.driver.execute_script("seetest:client.deviceAction(\"BKSP\")")
    self.driver.execute_script("seetest:client.sendText(\"Ga\")")
    self.driver.swipe(304, 536, 304, 116, 885)
    self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()

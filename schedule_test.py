import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class test_schedule_test(unittest.TestCase):
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

    def test_add_new_schedule(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='check' and (./preceding-sibling::* | ./following-sibling::*)[@text='A']]").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='SAVE']")))
        self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.EditText' and ./parent::*[./parent::*[@id='inputDate']]]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='26']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='inputTimeEditText']").click()
        self.driver.swipe(364, 608, 408, 660, 2311)
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()


    def test_add_multiple_new_schedules(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='SCHEDULE']]").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='sd_main_fab']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='sd_main_fab']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='NEW PLAN']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='NEW PLAN']")))
        self.driver.find_element_by_xpath("xpath=//*[@text='NEW PLAN']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='ADD CUSTOMERS']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='check' and (./preceding-sibling::* | ./following-sibling::*)[@text='7 to 7 supermarket']]")))
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='check' and (./preceding-sibling::* | ./following-sibling::*)[@text='7 to 7 supermarket']]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='check' and (./preceding-sibling::* | ./following-sibling::*)[@text='A to Z TEXTILE']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.EditText']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@class='android.widget.EditText']")))
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.EditText']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='21']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='SAVE']")))
        self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()

    def test_duplicate_schedule(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='SCHEDULE']]").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//*[@id='tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='SCHEDULE']]")))
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='SCHEDULE']]").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='sd_main_fab']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='sd_main_fab']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='DUPLICATE SCHEDULE']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='SELECT SCHEDULE TITLE']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='(NO SCHEDULE TITLE)' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fri, 21 Aug']]")))
        self.driver.find_element_by_xpath(
            "xpath=//*[@text='(NO SCHEDULE TITLE)' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fri, 21 Aug']]").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='checkBox' and (./preceding-sibling::* | ./following-sibling::*)[@text='7 to 7 supermarket']]")))
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='checkBox' and (./preceding-sibling::* | ./following-sibling::*)[@text='7 to 7 supermarket']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.EditText']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='26']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='SAVE']")))
        self.driver.find_element_by_xpath("xpath=//*[@text='SAVE']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

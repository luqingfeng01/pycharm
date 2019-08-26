from time import sleep
from appium import webdriver
import unittest


desired_caps = {'platformName':'Android',
                'deviceName':'127.0.0.1:62001',
                'platformVersion':'3.8.3.1',
                'appPackage':'com.kredito.fintek',
                'appActivity':'com.lepin.danabersama.ui.activity.MainActivity'
                }
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
sleep(4)

driver.find_element_by_id("com.kredito.fintek:id/versionchecklib_version_dialog_cancel").click()
sleep(3)
driver.find_element_by_id("com.kredito.fintek:id/messages").click()
sleep(3)
driver.find_element_by_id("com.kredito.fintek:id/userNameTv").click()
sleep(2)
driver.find_element_by_id("com.kredito.fintek:id/phoneEdit").send_keys("15820797938")
driver.find_element_by_id("com.kredito.fintek:id/pwdEdit").send_keys("qwer1234")
sleep(2)
driver.find_element_by_id("com.kredito.fintek:id/loginBtn")

sleep(5)
driver.quit()
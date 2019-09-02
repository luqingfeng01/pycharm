from time import sleep
from appium import webdriver
import unittest

from time import sleep
from appium import webdriver
desired_caps = {'platformName':'Android',
                'deviceName':'127.0.0.1:62001',
                'platformVersion':'3.8.3.1',
                'appPackage':'com.juyang.mall',
                'appActivity':'com.shanjian.juyang.activity.home.Activity_Home'
                }
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
sleep(4)
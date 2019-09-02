from time import sleep
from appium import webdriver
import unittest,random
from appiummaster.untils.AppiumServer import AppiumServer





from time import sleep
from appium import webdriver
desired_caps = {'platformName':'Android',
                'deviceName':'127.0.0.1:62001',
                'platformVersion':'3.8.3.1',
<<<<<<< HEAD
                'appPackage':'com.juyang.mall',
                'appActivity':'com.shanjian.juyang.activity.home.Activity_Home'
=======
                'appPackage':'com.kredito.fintek',
                'appActivity':'com.lepin.danabersama.ui.activity.MainActivity',
                'automationName':'Appium',
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
>>>>>>> 910a05506b440b75c247450209fbb500c24776f3
                }
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
sleep(4)
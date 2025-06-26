
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from time import sleep
import unittest, time, os
from selenium.webdriver.support.wait import WebDriverWait
import allure



@pytest.fixture()
def conexionappium():

    cap: dict[str,any] ={
           "platformName": "Android",
           "appium:deviceName": "a52q",
           "appium:automationName": "UiAutomator2",
           "appium:appPackage": "com.eset.ems2.gp",
           "appium:appActivity": "com.eset.ems.gui.MainActivityAlias",
           "appium:platformVersion": "14"
    }
    url= 'http://192.168.0.8:4723'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    return driver



    


from time import sleep
from selenium import webdriver
#from web.setup.principal import base_url
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import os
from selenium.webdriver import Chrome
import pytest

url, driver = configurardatos()

# @pytest.mark.parametrize("driver", [
# (webdriver.Chrome(options=opt)),
# (webdriver.Edge()),
#  (webdriver.Firefox()),
# ])



def test_dashboard():
    driver.get(url=url)
    assert "Welcome!" == driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div/h1').text
    # driver.close()


def test_login():
    driver.get(url=url)
    driver.find_element(by=By.XPATH, value='//*[@id="auth-shop"]/b').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email"]').send_keys('admin@admin.com')
    driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('admin123')
    driver.find_element(by=By.ID, value='submitLoginBtn').click()
    sleep(4)
    assert "SHOPPING CART" == driver.find_element(by=By.XPATH, value='//*[@id="prooood"]/section[1]/h2').text
    #driver.close()

def test_exito():
    assert 1 == 1

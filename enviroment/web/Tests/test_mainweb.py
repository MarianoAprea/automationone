from time import sleep
from selenium import webdriver
#from web.setup.principal import base_url
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import os
from selenium.webdriver import Chrome
#from webdriver_manager.core.os_manager import ChromeType
import pytest

base_url ='https://qa-practice.netlify.app/'

opt = Options()

opt.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
opt.add_argument("--no-sandbox")
opt.add_argument("--incognito")
opt.add_argument("--disable-extensions")
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('log-level=3')
opt.add_argument('--disable-dev-shm-usage')
opt.add_argument('--aggressive-cache-discard')

opt.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service('/usr/local/bin/chromedriver')


# @pytest.mark.parametrize("driver", [
# (webdriver.Chrome(options=opt)),
# (webdriver.Edge()),
#  (webdriver.Firefox()),
# ])
def test_dashboard():
    driver = webdriver.Chrome(service=service, options=opt)
    # driver = webdriver.Chrome(options=opt, service=Service(executable_path="/usr/local/bin/chromedriver"))
    driver.get(url=base_url)
    assert "Welcome!" == driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div/h1').text
    driver.quit()


def test_login():
    driver = webdriver.Chrome(service=service, options=opt)
    driver.get(url=base_url)
    driver.find_element(by=By.XPATH, value='//*[@id="auth-shop"]/b').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email"]').send_keys('admin@admin.com')
    driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('admin123')
    driver.find_element(by=By.ID, value='submitLoginBtn').click()
    sleep(1)
    assert "SHOPPING CART" == driver.find_element(by=By.XPATH, value='//*[@id="prooood"]/section[1]/h2').text
    driver.quit()

def test_exito():
    assert 1 == 1

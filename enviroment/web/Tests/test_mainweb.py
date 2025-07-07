from time import sleep
from selenium import webdriver
#from web.setup.principal import base_url
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

base_url ='https://qa-practice.netlify.app/'

opt = webdriver.ChromeOptions()
#opt.add_argument("--headless")  #  ejecuta sin mostrar el  navegador
#opt.add_argument("--user-data-dir=/tmp/user-data")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-extensions")
opt.add_argument('--ignore-certificate-errors')
#opt.add_argument("--enable-automation")  #  muestra la barra de que es manejado por un automatizador

# @pytest.mark.parametrize("driver", [
#  (webdriver.Chrome()),
# (webdriver.Edge()),
#  (webdriver.Firefox()),
# ])

def test_login():
    driver = webdriver.Chrome(options=opt)
    driver.get(url=base_url)
    assert "Welcome!" == driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div/h1').text
    driver.find_element(by=By.XPATH, value='//*[@id="auth-shop"]/b').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email"]').send_keys('admin@admin.com')
    driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('admin123')
    driver.find_element(by=By.ID, value='submitLoginBtn').click()
    sleep(1)
    assert "SHOPPING CART" == driver.find_element(by=By.XPATH, value='//*[@id="prooood"]/section[1]/h2').text
    driver.quit()

from time import sleep
from selenium import webdriver
#from web.setup.principal import base_url
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opt = Options()  # the variable that will store the selenium options
opt.add_argument(
    '--user-data-dir=' + r'C:\Users\Estudiante\AppData\Local\Google\Chrome\User Data')  # Add the user data path as an argument in selenium Options
opt.add_argument('--profile-directory=Default')  # Add the profile directory as an argument in selenium Options
# s = Service('C:/Users/ResetStoreX/AppData/Local/Programs/Python/Python39/Scripts/chromedriver.exe')

base_url ='https://qa-practice.netlify.app/'


@pytest.mark.parametrize("driver", [
    (webdriver.Chrome())  #(webdriver.Edge()), (webdriver.Firefox()),
])
def test_loginOK(driver):

    driver.get(url=base_url)
    assert "Welcome!" == driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div/h1').text
    driver.find_element(by=By.XPATH, value='//*[@id="auth-shop"]/b').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email"]').send_keys('admin@admin.com')
    driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('admin123')
    driver.find_element(by=By.ID, value='submitLoginBtn').click()
    sleep(1)
    assert "SHOPPING CART" == driver.find_element(by=By.XPATH, value='//*[@id="prooood"]/section[1]/h2').text
    driver.quit()

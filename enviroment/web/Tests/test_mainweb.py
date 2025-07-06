from time import sleep
from selenium import webdriver
#from web.setup.principal import base_url
from selenium.webdriver.common.by import By
import pytest

# if __name__ == "__main__":
#  pytest.main(["test_mainweb.py"])

base_url ='https://qa-practice.netlify.app/'

# @pytest.mark.parametrize("driver", [
#   (webdriver.Chrome()),
    #(webdriver.Edge()), (webdriver.Firefox()),
#])

driver = webdriver.Chrome()


def test_loginOK():

    driver.get(url=base_url)
    assert "Welcome!" == driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[1]/div/h1').text
    driver.find_element(by=By.XPATH, value='//*[@id="auth-shop"]/b').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email"]').send_keys('admin@admin.com')
    driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('admin123')
    driver.find_element(by=By.ID, value='submitLoginBtn').click()
    sleep(1)
    assert "SHOPPING CART" == driver.find_element(by=By.XPATH, value='//*[@id="prooood"]/section[1]/h2').text
    driver.quit()

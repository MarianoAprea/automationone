from src.main import conexionappium

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
import time
import allure

# time.sleep(1)
driver = conexionappium


#@allure.tag("text_processor")
#@allure.title("Test count_words function")
#@allure.description("Test the count_words function")
#@allure.severity(allure.severity_level.Critical)

@allure.step("Step 1")
#@allure.description("Abre lista de paises")
#@allure.severity(allure.severity(critical))

def test_show_country_list(driver):
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/country_selector').click()
    assert "Seleccione su país"==(driver.find_element(by=By.XPATH, value='//android.widget.TextView[@resource-id="com.eset.ems2.gp:id/title"]').get_attribute("text"))

@allure.step("Step 2")
@allure.description("Selecciona un pais de la lista")

def test_select_a_countryfromlist(driver):
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/country_selector').click()
    driver.find_element(by=By.XPATH, value='//android.widget.CheckedTextView[@text="Australia"]').click()
    assert "AUS" == (driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/country_selector').get_attribute("text"))
@allure.step("Step 3")
def test_select_a_countryfromBuscar(driver):
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/country_selector').click()
    driver.find_element(by=By.XPATH,value='//android.widget.EditText[@resource-id="com.eset.ems2.gp:id/search"]').send_keys('brasil')
    assert "Brasil" == (driver.find_element(by=By.XPATH, value='//android.widget.CheckedTextView[@text="Brasil"]').get_attribute("text"))
@allure.step("Step 4")
def test_select_personalizaryveopciones(driver):
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/secondary_button').click()
    driver.find_element(by=By.XPATH,value='//android.widget.Button[@resource-id="com.eset.ems2.gp:id/expand_live_grid_button"]').click()
    driver.find_element(by=By.ID,value='com.eset.ems2.gp:id/live_grid_checkbox').click()
    driver.find_element(by=By.XPATH,value='//android.widget.Button[@resource-id="com.eset.ems2.gp:id/expand_live_grid_button"]').click()

    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/expand_analytics_button').click()
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/analytics_checkbox').click()
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/expand_analytics_button').click()

    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/expand_data_usage_button').click()
    driver.find_element(by=By.XPATH, value='//android.widget.Button[@resource-id="com.eset.ems2.gp:id/expand_data_usage_button"]').click()
    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/expand_data_usage_button').click()

    driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/offers_checkbox').click()
@allure.step("Step 5")
def test_select_continuarwithoutselected(driver):
        driver.find_element(by=By.ID, value='com.eset.ems2.gp:id/secondary_button').click()
        driver.find_element(by=By.XPATH, value='//android.widget.Button[@resource-id="com.eset.ems2.gp:id/continue_button"]').click()
        driver.find_element(by=By.XPATH, value='//android.widget.Button[@resource-id="com.eset.ems2.gp:id/continue_free_button"]').click()
        time.sleep(10)
        assert "Iniciar análisis" == driver.find_element(by=By.XPATH,value='//android.widget.Button[@resource-id="com.eset.ems2.gp:id/action_button"]').get_attribute("text")

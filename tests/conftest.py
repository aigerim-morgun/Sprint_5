import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators
from helpers import generate_email, generate_password
from urls import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL)
    driver.find_element(*RegisterPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aigerim")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.EMAIL_INPUT))

    return email, password

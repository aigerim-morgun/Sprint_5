from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators
from helpers import generate_email, generate_password, generate_short_password
from urls import BASE_URL


def test_registration(driver):
    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL)
    driver.find_element(*RegisterPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aigerim")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))

    assert "login" in driver.current_url


def test_registration_short_password(driver):
    email = generate_email()
    short_password = generate_short_password()

    driver.get(BASE_URL)
    driver.find_element(*RegisterPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aigerim")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(short_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))

    assert "Некорректный пароль" in error_message.text
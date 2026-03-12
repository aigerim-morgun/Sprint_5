from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegisterPageLocators

def test_registration(generate_email, generate_password):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*RegisterPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "name")))
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aigerim")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains("login"))

    assert "login" in driver.current_url

    driver.quit()


def test_registration_short_password(generate_email, generate_short_password):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*RegisterPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "name")))
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aigerim")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_short_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))

    assert "Некорректный пароль" in error_message.text

    driver.quit()
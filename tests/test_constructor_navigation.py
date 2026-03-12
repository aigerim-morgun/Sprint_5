from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorPageLocators, LoginPageLocators


def test_transition_from_account_to_constructor(driver, registered_user):

    email, password = registered_user

    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))

    driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"


def test_transition_from_account_by_logo(driver, registered_user):

    email, password = registered_user

    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains("account"))

    driver.find_element(*ConstructorPageLocators.LOGO).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"
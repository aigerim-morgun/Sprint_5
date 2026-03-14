from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorPageLocators, LoginPageLocators
from urls import BASE_URL, LOGIN_PAGE


def test_transition_from_account_to_constructor(driver, registered_user):
    email, password = registered_user

    driver.get(LOGIN_PAGE)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON).click()

    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(BASE_URL))


def test_transition_from_account_by_logo(driver, registered_user):
    email, password = registered_user

    driver.get(LOGIN_PAGE)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*ConstructorPageLocators.LOGO).click()

    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(BASE_URL))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegisterPageLocators, LoginPageLocators


def test_login_ffrom_main_page(driver, registered_user):
    email, password = registered_user

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))

    assert "Оформить заказ" in order_button.text


def test_login_from_personal_account(driver, registered_user):

    email, password = registered_user

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_contains("login"))

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))

    assert "Оформить заказ" in order_button.text


def test_login_from_registration_page(driver, registered_user):

    email, password = registered_user

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_contains("login"))
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()
   
    driver.find_element(*LoginPageLocators.LOGIN_LINK).click()

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))

    assert "Оформить заказ" in order_button.text


def test_login_from_forgot_password_page(driver, registered_user):

    email, password = registered_user

    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_contains("login"))
    driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()

    driver.find_element(*LoginPageLocators.LOGIN_LINK).click()

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))

    assert "Оформить заказ" in order_button.text

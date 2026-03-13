from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators, ProfilePageLocators
from urls import BASE_URL

def test_logout_from_personal_account(driver, registered_user):
    email, password = registered_user

    driver.get(BASE_URL)
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    login_form_visible = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
    

    assert login_form_visible.is_displayed()
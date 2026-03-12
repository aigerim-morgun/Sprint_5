import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import RegisterPageLocators

@pytest.fixture
def generate_email():
    number = random.randint(100, 999)
    return f"aigerimmorgun36{number}@yandex.ru"


@pytest.fixture
def generate_password():
    return str(random.randint(100000, 999999))


@pytest.fixture
def generate_short_password():
    return str(random.randint(1000, 9999))


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def registered_user(driver):
    email = f"aigerimmorgun36{random.randint(100,999)}@yandex.ru"
    password = str(random.randint(100000,999999))

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*RegisterPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*RegisterPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aigerim")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.url_contains("login"))

    return email, password

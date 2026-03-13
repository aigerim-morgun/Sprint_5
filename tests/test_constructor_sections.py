from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorPageLocators
from urls import BASE_URL


def test_open_buns_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()

    driver.find_element(*ConstructorPageLocators.BUNS_SECTION).click()

    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstructorPageLocators.BUNS_ACTIVE))


def test_open_sauces_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()

    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstructorPageLocators.SAUCES_ACTIVE))


def test_open_fillings_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).click()

    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstructorPageLocators.FILLINGS_ACTIVE))
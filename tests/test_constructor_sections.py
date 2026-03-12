from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorPageLocators

def test_open_buns_section(driver):

    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ConstructorPageLocators.BUNS_ACTIVE))

    assert driver.find_element(*ConstructorPageLocators.BUNS_ACTIVE)


def test_open_sauces_section(driver):

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()

    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(ConstructorPageLocators.SAUCES_ACTIVE))

    assert "Соусы" in driver.page_source


def test_open_fillings_section(driver):

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).click()

    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(ConstructorPageLocators.FILLINGS_ACTIVE))

    assert "Начинки" in driver.page_source
from selenium.webdriver.common.by import By

class RegisterPageLocators: # Регистрация
    # Поле ввода "Имя":
    NAME_INPUT = (By.NAME, "name")
    # Поле ввода "Email":
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода "Пароль":
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Зарегистрироваться":
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке "Некорректный пароль":
    PASSWORD_ERROR = (By.CSS_SELECTOR, "p.input__error")
    # Кнопка "Войти в аккаунт":
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Гиперссылка "Зарегистрироваться":
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")


class LoginPageLocators: # Вход по кнопке «Войти в аккаунт»
    # Поле ввода "Email":
    EMAIL_INPUT = (By.XPATH, "//div[@class='Auth_login__3hAey']//input[@name='name']")
    # Поле ввода "Пароль":    
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    # Кнопка "Войти":
    LOGIN_BUTTON = (By.XPATH, "//div[@class='Auth_login__3hAey']//button[text()='Войти']")
    # Кнопка "Оформить заказ" на главной странице:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Кнопка "Личный Кабинет":
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    # Гиперссылка "Войти" в форме регистрации:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    # Гиперссылка "Восстановить пароль":
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


class ConstructorPageLocators:
    # Кнопка "Конструктор":
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers:
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    # Вкладка "Булки" в навигации конструктора:
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    # Вкладка "Соусы" в навигации конструктора:
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    # Вкладка "Начинки" в навигации конструктора:
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    # активная вкладка "Булки":
    BUNS_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current') and .//span[text()='Булки']]")
    # активная вкладка "Соусы":
    SAUCES_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current') and .//span[text()='Соусы']]")
    # активная вкладка "Начинки":
    FILLINGS_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current') and .//span[text()='Начинки']]")


class ProfilePageLocators:
    # кнопка "Выйти" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
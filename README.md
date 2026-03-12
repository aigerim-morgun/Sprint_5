   Stellar Burgers — Автоматизированные тесты


Этот проект содержит автоматизированные UI-тесты для сайта Stellar Burgers: https://stellarburgers.education-services.ru/, с использованием Selenium + Python + Pytest.

Тесты проверяют регистрацию, вход, выход из аккаунта, навигацию по разделам конструктора и личного кабинета.

Проект рассчитан на Python 3.14+


   Структура проекта:
Sprint_5/
  -conftest.py 
  -README.md
  -tests/
      -locators.py
      -test_login.py
      -test_logout.py
      -test_registration.py
      -test_profile_navigation.py
      -test_constructor_navigation.py
      -test_constructor_sections.py

    
   Запуск тестов:
Запуск всех тестов: pytest -s tests
Запуск конкретного файла: pytest -s tests/test_login.py
Запуск с подробным выводом: pytest -v tests

   Фикстуры:
driver - создает и закрывает ChromeDriver;

registered_user - регистрирует нового пользователя через форму регистрации и возвращает и email password;

generate_short_password - генерирует короткий пароль (4 символа);

generate_email - генерирует email;

generate_password - генерирует пароль (6 символов).


Основные тесты
	1.	test_login.py
		-Вход с главной страницы
		-Вход из личного кабинета
		-Вход через форму восстановления пароля
		-Вход через форму регистрации
	2.	test_logout.py
		-Выход из аккаунта через кнопку «Выйти»
	3.	test_registration.py
		-Регистрация нового пользователя
	4.	test_profile_navigation.py
		-Переход в личный кабинет
		-Переход из личного кабинета в конструктор
	5.	test_constructor_sections.py
		-Переход по вкладкам конструктора: Булки, Соусы, Начинки
	6.	test_constructor_navigation.py
		-Переход по разделам конструктора
		-Переход по клику на логотип Stellar Burgers

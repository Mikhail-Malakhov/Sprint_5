# Sprint_5 — автотесты для Stellar Burgers

UI-автотесты на Selenium + pytest для сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/).

## Структура проекта

| Файл / папка | Назначение |
|---|---|
| `data.py` | URL страниц, данные для генерации почты, таймаут ожиданий |
| `locators.py` | Локаторы элементов с комментариями |
| `helpers.py` | Генераторы логина (email), пароля, имени и данных пользователя; ожидания, регистрация, вход, переключение вкладок конструктора |
| `conftest.py` | Все фикстуры: `driver`, `registered_user`, `logged_in_driver` (без генерации данных внутри) |
| `tests/test_registration.py` | Регистрация: успешная, ошибка при некорректном пароле |
| `tests/test_login.py` | Вход: с главной («Войти в аккаунт»), через «Личный кабинет», из формы регистрации, из формы восстановления пароля |
| `tests/test_personal_account.py` | Переход в личный кабинет, переход в конструктор (кнопка «Конструктор» и логотип), выход из аккаунта |
| `tests/test_constructor.py` | Переходы к разделам «Булки», «Соусы», «Начинки» |

## Запуск

```bash
pip install -r requirements.txt
pytest -v                      # Google Chrome (по умолчанию)
pytest -v --browser=firefox    # Mozilla Firefox
```
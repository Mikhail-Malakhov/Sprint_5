class Urls:
    MAIN = "https://stellarburgers.education-services.ru/"            # Главная страница (конструктор)
    LOGIN = MAIN + "login"                                             # Страница входа
    REGISTER = MAIN + "register"                                       # Страница регистрации
    FORGOT_PASSWORD = MAIN + "forgot-password"                         # Страница восстановления пароля
    PROFILE = MAIN + "account/profile"                                 # Личный кабинет (профиль)


class UserData:
    # Данные для генерации уникальной почты: имя_фамилия_номер когорты_3 цифры@домен
    NAME = "mikhail"
    SURNAME = "malakhov"
    COHORT = "55"
    DOMAIN = "yandex.ru"


TIMEOUT = 10  # Время ожидания элементов, сек.

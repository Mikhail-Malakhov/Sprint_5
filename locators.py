from selenium.webdriver.common.by import By


class HeaderLocators:
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")                       # Кнопка «Личный кабинет» в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")              # Кнопка «Конструктор» в шапке
    LOGO = (By.XPATH, "//div[contains(@class, 'header__logo')]//a")                   # Логотип Stellar Burgers в шапке


class CommonLocators:
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")      # Затемняющий слой (оверлей) поверх страницы при загрузке


class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")        # Кнопка «Войти в аккаунт» на главной
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")              # Кнопка «Оформить заказ» (видна только после входа)
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")                  # Заголовок «Соберите бургер»
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")                       # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")                     # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")                 # Вкладка «Начинки»
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")        # Активная (выбранная) вкладка конструктора


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")         # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")      # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")                            # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")             # Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")                                    # Ссылка «Войти» под формой регистрации
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")                  # Сообщение об ошибке «Некорректный пароль»


class LoginPageLocators:
    TITLE = (By.XPATH, "//h2[text()='Вход']")                                         # Заголовок формы «Вход»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")      # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")                            # Поле «Пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")                             # Кнопка «Войти»
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")                    # Ссылка «Зарегистрироваться»
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")           # Ссылка «Восстановить пароль»


class ForgotPasswordPageLocators:
    TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")                        # Заголовок «Восстановление пароля»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")                                    # Ссылка «Войти» под формой восстановления


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")                                # Пункт меню «Профиль» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")                            # Кнопка «Выход» в личном кабинете

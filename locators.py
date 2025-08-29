from selenium.webdriver.common.by import By

class Locators:

    #Кнопка "Войти в аккаунт" на главной странице
    entrance_on_the_main = (By.XPATH, "//button[text()='Войти в аккаунт]")

    #Основной логотип
    logo = (By.XPATH, '//header/nav/div')

    #Надпись "Выход"
    button_exit = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    #Надпись "Профиль"
    ins_profile = (By.XPATH, './/a[@href="/account/profile"]')

    #Надпись "Булки"
    ins_bred = (By.XPATH, ".//span[contains(text(), 'Булки')]")

    #Кнопка "Личный кабинет"
    button_personal = (By.XPATH, ".//p[contains(text(), 'Личный кабинет')]")

    #Надпись "Соусы"
    ins_sauce = (By.XPATH, ".//span[contains(text(), 'Соусы')]")

    #Надпись "Зарегистрироваться"
    ins_login = (By.CLASS_NAME, "Auth_link__1f01j")

    #Надпись "Начинки"
    ins_fillings = (By.XPATH, ".//span[contains(text(), 'Начинки')]")

    #Надпись "Такой пользователь уже существует"
    ins_error_account = (By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")

    #Надпись "Некорректный пароль"
    ins_error_password = (By.XPATH, "//div[contains(@class, 'input_status_error')]")

    #Кнопка "Восстановить пароль"
    button_restore_password = (By.XPATH, ".//a[@href='/forgot-password']")

    #Кнопка_надпись "Войти"
    ins_button_entrance = (By.XPATH, ".//a[@href='/login']")

    #Кнопка "Войти"
    button_entrance = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    #Кнопка "Оформить заказ"
    button_arrange_order = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")

    #Кнопка зарегистрировать
    button_login = (By.XPATH, ".//button[contains(text(), 'Зарегистрировать')]")

    #Кнопка "Конструктор"
    button_const = (By.XPATH, ".//a[@href='/']")

    #Поле Имя
    field_name = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input")

    #Поле Email
    field_email = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")

    #Поле Пароль
    fiel_password = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")    

    #Активный раздел
    active_section = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
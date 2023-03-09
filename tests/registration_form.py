from time import sleep
from selenium.webdriver.support import expected_conditions
from config.elements import TestLocators
from config.data_generation import mail, number_of_user, password
from selenium.webdriver.support.wait import WebDriverWait

#проверка наличия кнопки регистрации в форме авторизации
def test_reg_form_from_button_on_main(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(TestLocators.REG_BUTTON_FROM_AUTH))

# проверка описания кнопки регистрации
def test_check_text_near_button_of_registration(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    assert 'Вы — новый пользователь?' in browser.find_element(*TestLocators.AUTH_FORM).text, \
        'описание не соовтествует макетам'

#  Переход на страницу регистрации
def test_to_open_reg_form(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.TITLE_FROM_REG).text == 'Регистрация' #проверка заголовка формы
#проверки плейсхолдеров
    sleep(1)
    assert 'Имя' in browser.find_element(*TestLocators.PLACEHOLDER_NAME_REG).text
    assert 'Email' in browser.find_element(*TestLocators.PLACEHOLDER_MAIL_REG).text
    assert 'Пароль' in browser.find_element(*TestLocators.PLACEHOLDER_PWD_REG).text
    assert 'Зарегистрироваться' in browser.find_element(*TestLocators.REG_BUTTON_FROM_REG).text

# заполнение полей регистрации
def test_complete_registration(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    browser.find_element(*TestLocators.NAME_INPUT_FROM_REG).send_keys(number_of_user())
    browser.find_element(*TestLocators.MAIL_INPUT_FROM_REG).send_keys(mail())
    browser.find_element(*TestLocators.PASS_INPUT_FROM_REG).send_keys(password())
    browser.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_FROM_AUTH))

# #проверка без заполненного поля
def test_registration_without_text_in_inputs(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    browser.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_FROM_REG))
# #пароль <6 симв
def test_registrarion_with_wrong_pwd(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    browser.find_element(*TestLocators.PASS_INPUT_FROM_REG).send_keys('Qwert')
    browser.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    WebDriverWait(browser, 1).until(expected_conditions.presence_of_element_located(TestLocators.ERROR_OF_PWD))

# #регистрация с пустым именем
def reg_without_name(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    browser.find_element(*TestLocators.MAIL_INPUT_FROM_REG).send_keys(mail())
    browser.find_element(*TestLocators.PASS_INPUT_FROM_REG).send_keys(password())
    browser.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_FROM_REG))



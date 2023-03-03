from time import sleep
from selenium import webdriver
from config.elements import TestLocators
from config.data_generation import mail, number_of_user, password


#проверка наличия кнопки регистрации в форме авторизации
def test_reg_form_from_button_on_main():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    sleep(1)
    assert driver.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).text == 'Зарегистрироваться'
    driver.quit()

# проверка описания кнопки регистрации
def test_check_text_near_button_of_registration():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    assert 'Вы — новый пользователь?' in driver.find_element(*TestLocators.AUTH_FORM).text, \
        'описание не соовтествует макетам'
    driver.quit()

#  Переход на страницу регистрации
def test_to_open_reg_form():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    assert driver.find_element(*TestLocators.TITLE_FROM_REG).text == 'Регистрация' #проверка заголовка формы
#проверки плейсхолдеров
    sleep(1)
    assert 'Имя' in driver.find_element(*TestLocators.PLACEHOLDER_NAME_REG).text
    assert 'Email' in driver.find_element(*TestLocators.PLACEHOLDER_MAIL_REG).text
    assert 'Пароль' in driver.find_element(*TestLocators.PLACEHOLDER_PWD_REG).text
    assert 'Зарегистрироваться' in driver.find_element(*TestLocators.REG_BUTTON_FROM_REG).text
    driver.quit()

# заполнение полей регистрации
def test_complete_registration():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    driver.find_element(*TestLocators.NAME_INPUT_FROM_REG).send_keys(number_of_user())
    driver.find_element(*TestLocators.MAIL_INPUT_FROM_REG).send_keys(mail())
    driver.find_element(*TestLocators.PASS_INPUT_FROM_REG).send_keys(password())
    driver.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    sleep(1)
    assert driver.find_element(*TestLocators.TITLE_FROM_AUTH).text == 'Вход'
    driver.quit()

# #проверка без заполненного поля
def test_registration_without_text_in_inputs():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    driver.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    sleep(1)
    assert 'Регистрация' in driver.find_element(*TestLocators.TITLE_FROM_REG).text
    driver.quit()
# #пароль <6 симв
def test_registrarion_with_wrong_pwd():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    driver.find_element(*TestLocators.PASS_INPUT_FROM_REG).send_keys('Qwert')
    driver.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    sleep(1)
    assert 'Некорректный пароль' in driver.find_element(*TestLocators.CONTAINER_OF_PWD_INPUT).text
    driver.quit()

# #регистрация с пустым именем
def reg_without_name():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.REG_BUTTON_FROM_AUTH).click()
    driver.find_element(*TestLocators.MAIL_INPUT_FROM_REG).send_keys(mail())
    driver.find_element(*TestLocators.PASS_INPUT_FROM_REG).send_keys(password())
    driver.find_element(*TestLocators.REG_BUTTON_FROM_REG).click()
    sleep(1)
    assert 'Регистрация' in driver.find_element(*TestLocators.TITLE_FROM_REG).text
    driver.quit()



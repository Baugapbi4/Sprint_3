from selenium import webdriver
from config.elements import TestLocators

def test_auth_from_header():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert driver.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'
    driver.quit()


def test_auth_from_order():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert driver.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'
    driver.quit()

def test_auth_from_reg():
    url = 'https://stellarburgers.nomoreparties.site/register'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_REG).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert driver.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'
    driver.quit()
def test_log_in_from_reset_pwd():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    driver.find_element(*TestLocators.RESET_BUTTON_FROM_AUTH).click()
    assert driver.find_element(*TestLocators.TITLE_FROM_RESET).text == 'Восстановление пароля'
    assert driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_RESET).text == 'Войти'
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_RESET).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert driver.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'
    driver.quit()
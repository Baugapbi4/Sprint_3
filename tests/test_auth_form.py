from config.elements import TestLocators

def test_auth_from_header(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'


def test_auth_from_order(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'

def test_auth_from_reg(browser):
    url = 'https://stellarburgers.nomoreparties.site/register'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_REG).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'
def test_log_in_from_reset_pwd(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_MAIN).click()
    browser.find_element(*TestLocators.RESET_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.TITLE_FROM_RESET).text == 'Восстановление пароля'
    assert browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_RESET).text == 'Войти'
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_RESET).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.LK_BUTTON).text == 'Личный Кабинет'

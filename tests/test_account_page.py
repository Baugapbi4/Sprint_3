from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config.elements import TestLocators


def test_check_list_pages(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    assert browser.find_element(*TestLocators.TITLE_FROM_AUTH)


def test_change_page_to_construct(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    browser.implicitly_wait(3)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.implicitly_wait(3)
    browser.find_element(*TestLocators.HEADER_BUTTON_CONSTRUCT).click()
    assert browser.find_element(*TestLocators.TITLE_FROM_MAIN).text == 'Соберите бургер'

def test_change_page_to_contruct_from_logo(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.HEADER_BUTTON_LOGO).click()
    assert browser.find_element(*TestLocators.TITLE_FROM_MAIN).text == 'Соберите бургер'

def test_logout_from_account(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    browser.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    browser.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    browser.implicitly_wait(2)
    browser.find_element(*TestLocators.LK_BUTTON).click()
    WebDriverWait(browser, 2).until(expected_conditions.element_to_be_clickable(TestLocators.LK_EXIT_BUTTON)).click()
    WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_FROM_AUTH))
    assert browser.find_element(*TestLocators.TITLE_FROM_AUTH).text == 'Вход'


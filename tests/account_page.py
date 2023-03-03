from time import sleep

from selenium import webdriver
from config.elements import TestLocators


def test_check_list_pages():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    driver.quit()

def test_change_page_to_contruct():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.HEADER_BUTTON_CONSTRUCT).click()
    assert driver.find_element(*TestLocators.TITLE_FROM_MAIN).text == 'Соберите бургер'
    driver.quit()

def test_change_page_to_contruct_from_logo():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.find_element(*TestLocators.HEADER_BUTTON_LOGO).click()
    assert driver.find_element(*TestLocators.TITLE_FROM_MAIN).text == 'Соберите бургер'
    driver.quit()

def test_logout_from_account():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FROM_AUTH).send_keys('Bartal_07_01@t.com')
    driver.find_element(*TestLocators.PASS_INPUT_FROM_AUTH).send_keys('qweqwe')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_FROM_AUTH).click()
    sleep(1)
    driver.find_element(*TestLocators.LK_BUTTON).click()
    driver.implicitly_wait(5)
    driver.find_element(*TestLocators.LK_EXIT_BUTTON)
    driver.quit()
from selenium import webdriver
from config.elements import TestLocators

def test_select_points_of_burger():
    url = 'https://stellarburgers.nomoreparties.site/'
    driver = webdriver.Chrome()
    driver.get(url)
    assert driver.find_element(*TestLocators.TITLE_OF_BREAD).text == 'Булки'
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.SAUCE_BUTTON).click()
    assert driver.find_element(*TestLocators.TITLE_OF_SAUCE).text == 'Соусы'
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.STUF_BUTTON).click()
    assert driver.find_element(*TestLocators.TITLE_OF_STUF).text == 'Начинки'
    driver.quit()
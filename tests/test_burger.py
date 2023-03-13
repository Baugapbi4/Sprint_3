from config.elements import TestLocators

def test_select_points_of_burger(browser):
    url = 'https://stellarburgers.nomoreparties.site/'
    browser.get(url)
    assert browser.find_element(*TestLocators.TITLE_OF_BREAD).text == 'Булки'
    browser.implicitly_wait(3)
    browser.find_element(*TestLocators.SAUCE_BUTTON).click()
    assert browser.find_element(*TestLocators.TITLE_OF_SAUCE).text == 'Соусы'
    browser.implicitly_wait(3)
    browser.find_element(*TestLocators.STUF_BUTTON).click()
    assert browser.find_element(*TestLocators.TITLE_OF_STUF).text == 'Начинки'

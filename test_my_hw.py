from selene import browser, by, have, be
import pytest

def test_first(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter().press_enter()
    browser.element('b').should(have.text('Об этой странице'))

def test_second(browser_size):
    browser.open('https://google.com"')
    browser.element('[name="text"]').should(be.blank).type('7675757гооопро').press_enter()
    browser.element('[class="card-section"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))
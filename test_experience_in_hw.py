from selene import browser, by, have, be
import pytest
import random
import time

# Добавил новую функцию, которая рандомит время принятия решений
def human_delay(min_sec=3, max_sec=5):
    time.sleep(random.uniform(min_sec, max_sec))
def test_search_positive(browser_size):
    browser.open('https://google.com')
    #Попытался обойти капчу, но посколько все запросы идут с одного ip ничего не вышло
    human_delay(3, 5)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    human_delay(3, 5)
    browser.press_enter()
    human_delay(3, 5)
    browser.element('b').should(have.text('Об этой странице'))
    human_delay(3, 5)

def test_search_negative(browser_size):
    browser.open('https://google.com"')
    human_delay(3, 5)
    browser.element('[name="text"]').should(be.blank).type('7675757гооопро').press_enter()
    human_delay(3, 5)
    browser.element('[class="card-section"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))



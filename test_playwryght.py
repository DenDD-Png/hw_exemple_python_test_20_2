from playwright.sync_api import Page, expect, Route
from time import sleep
#Регулярное выражение
import re
def test_paywright(page: Page):
    page.goto('https://ru.wikipedia.org/')
    page.get_by_role('link', name='Википедию').click()
    expect(page.get_by_text('Материал из Википедии — свободной энциклопедии')).to_be_visible()

def test_paywright2(page: Page):
    page.goto('https://ru.wikipedia.org/')
    page.get_by_role('link', name='Содержание').click()
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание')
    expect(page.get_by_text('Материал из Википедии — свободной энциклопедии')).to_be_visible()

#Попытка подмены трафика во время выполнения теста
def test_request(page: Page):
    #Новая функция обработчик информации результата перехватат re.compile
    def change_request(rout: Route):
        data = rout.request.post_data
        if data:
            data = data.replace('User412', 'sdfsdf')
        rout.continue_(post_data=data)

    # re.compile это поиск любого запроса в url которого есть profile/authenticate
    # В Playwright метод page.route() с регулярным выражением (re.compile) используется для перехвата и модификации сетевых запросов
    page.route(re.compile('profile/authenticate'),change_request)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    sleep(6)

def test_response(page: Page):
    def change_response(rout: Route):
        response = rout.fetch()
        data = response.text()
        data = data.replace('User412', 'Шапала824')
        rout.fulfill(response=response, body=data)

    page.route(re.compile('profile/412'), change_response)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    #В Playwright для подмены нужно куда-то нажать, выбор пал на профиль
    page.get_by_role('button', name='Мой профиль').click()
    sleep(6)

# Запус конкретного теста --slowmo=1000 для визуального понимания без спешки :D
# pytest test_playwryght.py::test_response -v -s --headed --slowmo=1000

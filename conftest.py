import pytest
from selene import browser

@pytest.fixture(scope = "function")
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()



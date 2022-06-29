import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    # options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--auto-open-devtools-for-tabs')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def driver(request, get_webdriver):
    driver = get_webdriver
    driver.set_window_size(1920, 1080)
    url = "https://bdas-utility-01.bdpak.frontier.kz:7002/"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://soundcloud.com/discover")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

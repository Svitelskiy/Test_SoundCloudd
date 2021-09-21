from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class DemoMainPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[@class='g-opacity-transition sc-button sc-button-medium loginButton']")
    CREATE_BUTTON = (By.XPATH, "//button[@class='g-opacity-transition sc-button sc-button-medium signupButton "
                               "sc-button-cta sc-button-primary']")


class DemoMainLocators:
    COOKIE_FILE = (By.ID, "onetrust-accept-btn-handler")
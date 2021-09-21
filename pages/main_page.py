from locators.main_page_locators import DemoMainPageLocators, DemoMainLocators


class HeaderPage:
    def __init__(self, browser):
        self.browser = browser

        self.create_button = self.browser.find_element(*DemoMainPageLocators.CREATE_BUTTON)

    def navigate_to_create_button(self):
        self.create_button.click()


class CookieFile:
    def __init__(self, browser):
        self.browser = browser

        self.cookie_button = self.browser.find_element(*DemoMainLocators.COOKIE_FILE)

    def navigate_to_cookie(self):
        self.cookie_button.click()

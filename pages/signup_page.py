from locators.signup_locators import SignUpWindowLocators, SignUpAfterContinue, SignUpAfterSubmit, SignUpDisplayName


class SignUpPage:
    def __init__(self, browser):
        self.browser = browser

        self.email_input = self.browser.find_element(*SignUpWindowLocators.EMAIL_INPUT)
        self.continue_button = self.browser.find_element(*SignUpWindowLocators.CONTINUE_BUTTON)
        self.password_input = self.browser.find_element(*SignUpAfterContinue.PASSWORD_INPUT)
        self.i_am_not_robot = self.browser.find_element(*SignUpAfterContinue.I_AM_NOT_ROBOT)
        self.submit_button = self.browser.find_element(*SignUpAfterContinue.SUBMIT_BUTTON)
        self.age_input = self.browser.find_element(*SignUpAfterSubmit.AGE_INPUT)
        self.gender_button = self.browser.find_element(*SignUpAfterSubmit.GENDER_BUTTON)
        self.submit_signup_button = self.browser.find_element(*SignUpAfterSubmit.SUBMIT_SIGNUP_BUTTON)
        self.display_name_input = self.browser.find_element(*SignUpDisplayName.DISPLAY_NAME_INPUT)
        self.get_started_button = self.browser.find_element(*SignUpDisplayName.GET_STARTED_BUTTON)

    def enter_valid_credentials(self, login):
        self.email_input.send_keys(login)
        self.continue_button.click()

    def enter_password(self, password):
        self.password_input.send_keys(password)
        self.i_am_not_robot.click()
        self.submit_button.click()

    def enter_age_and_gender(self):
        self.age_input.send_keys(18)
        self.gender_button.find_element("Male").click()
        self.submit_signup_button.click()

    def enter_user_name(self, display_name):
        self.display_name_input.send_keys(display_name)
        self.get_started_button.click()
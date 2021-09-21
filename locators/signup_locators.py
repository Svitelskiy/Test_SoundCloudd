from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class SignUpWindowLocators:
    EMAIL_INPUT = (By.ID, "sign_in_up_email")
    CONTINUE_BUTTON = (By.ID, "sign_in_up_submit")


@dataclass
class SignUpAfterContinue:
    PASSWORD_INPUT = (By.ID, "enter_password_field")
    I_AM_NOT_ROBOT = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    SUBMIT_BUTTON = (By.ID, "enter_password_submit")


@dataclass
class SignUpAfterSubmit:
    AGE_INPUT = (By.ID, "age")
    GENDER_BUTTON = (By.ID, "gender")
    SUBMIT_SIGNUP_BUTTON = (By.ID, "submit_signup")


@dataclass
class SignUpDisplayName:
    DISPLAY_NAME_INPUT = (By.ID, "sign_up_username")
    GET_STARTED_BUTTON = (By.ID, "sign_up_display_name_submit")




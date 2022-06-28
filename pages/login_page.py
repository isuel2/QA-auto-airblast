from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def enter_login_and_password(self, login, password):
        self.element_is_visible(self.locators.LOGIN_FORM).send_keys(login)
        self.element_is_visible(self.locators.PASSWORD_FORM).send_keys(password)

    def click_on_the_button(self):
        return self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

    def check_navigation_bar_title_login(self, login: str):
        all_list = self.locators.NAVIGATION_BAR
        all_list = (all_list[0], all_list[1].replace('*login*', login))
        all_list = [x.text for x in self.elements_are_visible(all_list)]
        return all_list

    def check_login_page_title_menu(self):
        all_list = self.elements_are_visible(self.locators.TITLE_LOGIN_PASSWORD_FORM, timeout=10)
        login_page = [x.text for x in all_list if len(x.text) > 0]
        return login_page

    def check_alert_insert_login(self):
        all_list = self.elements_are_visible(self.locators.TITLE_LOGIN_PASSWORD_FORM_ALERT_INSERT_LOGIN, timeout=10)
        login_page = [x.text for x in all_list if len(x.text) > 0]
        return login_page

    def check_alert_insert_password(self):
        all_list = self.elements_are_visible(self.locators.TITLE_LOGIN_PASSWORD_FORM_ALERT_INSERT_PASSWORD, timeout=10)
        login_page = [x.text for x in all_list if len(x.text) > 0]
        return login_page

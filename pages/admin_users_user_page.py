from pages.base_page import BasePage
from locators.admin_page_locators import UsersPageLocators
from generator.generator import generated_person
from selenium.webdriver.common.keys import Keys

department_drbi = 'DBRI'
department_dkb = 'DKB'
role_pak_bdw_admin = 'PAK_BDW_ADMIN'
role_pak_bdas_admin = 'PAK_BDAS_ADMIN'
group_kta = 'KTA'


class UsersCreatePage(BasePage):
    locators = UsersPageLocators()

    def create_user(self):
        self.element_is_present(self.locators.LIST_USER_SWITCH).click()
        self.element_is_present(self.locators.CREATE_USER).click()

    def fill_name_field(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        self.element_is_present(self.locators.FIRST_NAME_FORM).send_keys(first_name)
        return first_name

    def fill_required_fields(self):
        person_info = next(generated_person())
        fits_name = person_info.first_name
        last_name = person_info.last_name
        login = person_info.login
        password = person_info.password
        department = department_dkb
        roles = role_pak_bdw_admin
        groups = group_kta
        self.element_is_present(self.locators.FIRST_NAME_FORM).send_keys(fits_name)
        self.element_is_present(self.locators.LAST_NAME_FORM).send_keys(last_name)
        self.element_is_present(self.locators.LOGIN_FORM).send_keys(login)
        self.element_is_present(self.locators.PASSWORD_FORM).send_keys(password)
        self.element_is_present(self.locators.DEPARTMENTS_FORM).send_keys(department, Keys.ENTER)
        self.element_is_present(self.locators.ROLES_FORM).send_keys(roles, Keys.ENTER)
        self.element_is_present(self.locators.GROUPS_FORM).send_keys(groups, Keys.ENTER)
        return fits_name, last_name, login, password, department, roles, groups

    def fill_additional_fields(self):
        person_info = next(generated_person())
        email = person_info.email
        phone = person_info.phone
        telegram = person_info.telegram
        self.element_is_present(self.locators.EMAIL_FORM).send_keys(email)
        self.element_is_present(self.locators.PHONE_FORM).send_keys(phone)
        self.element_is_present(self.locators.TELEGRAM_FORM).send_keys(telegram)
        return email, phone, telegram

    def fill_name_field_cyrillic(self):
        first_name = "Пользователь"
        self.element_is_present(self.locators.FIRST_NAME_FORM).send_keys(first_name)
        return first_name

    def click_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def check_all_required_form(self):
        first_name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.FIRST_NAME_FORM)][0]
        last_name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.LAST_NAME_FORM)][0]
        login = [x.get_attribute('value') for x in self.elements_are_present(self.locators.LOGIN_FORM)][0]
        password = [x.get_attribute('value') for x in self.elements_are_present(self.locators.PASSWORD_FORM)][0]
        department = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DEPARTMENTS_FORM)][0]
        roles = [x.get_attribute('value') for x in self.elements_are_present(self.locators.ROLES_FORM)][0]
        groups = [x.get_attribute('value') for x in self.elements_are_present(self.locators.GROUPS_FORM)][0]
        return first_name, last_name, login, password, department, roles, groups

    def check_first_name_fill_form(self):
        first_name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.FIRST_NAME_FORM)][0]
        return first_name

    def check_perm_list_table(self):
        perms = [x.text for x in self.elements_are_present(self.locators.LIST_PERM_TD)]
        return perms

    def check_form_in_list_by_name(self, first_name: str):
        list_elements = self.locators.USER_IN_OVERALL_LIST
        list_elements = (list_elements[0], list_elements[1].replace('*first_name*', first_name))
        list_elements = [x.text for x in self.elements_are_present(list_elements)]
        return list_elements

    def click_to_form_by_name(self, first_name: str):
        temp = self.locators.LIST_USER_UPDATE_BUTTON
        temp = (temp[0], temp[1].replace('*first_name*', first_name))
        self.element_is_present(temp).click()

    def switch_to_user_list(self):
        self.element_is_present(self.locators.LIST_USER_SWITCH).click()

    def check_alert_name_form(self):
        all_list = self.elements_are_visible(self.locators.FIRST_NAME_ALERT, timeout=10)
        all_list = [x.text for x in all_list if len(x.text) > 0]
        return all_list

    def check_status_user(self, first_name: str):
        user_status = self.locators.LIST_USER_STATUS
        user_status = (user_status[0], user_status[1].replace('*first_name*', first_name))
        user_status = [x.text for x in self.elements_are_present(user_status)]
        return user_status

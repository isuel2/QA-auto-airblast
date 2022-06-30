from pages.base_page import BasePage
from locators.admin_page_locators import DepartmentsPageLocators
from generator.generator import generated_person


class DepartmentsCreatePage(BasePage):
    locators = DepartmentsPageLocators()

    def create_department(self):
        self.element_is_present(self.locators.LIST_DEPARTMENTS_SWITCH).click()
        self.element_is_present(self.locators.CREATE_DEPARTMENT).click()

    def fill_name_field(self):
        person_info = next(generated_person())
        name = person_info.name
        self.element_is_present(self.locators.DEPARTMENT_NAME_FORM).send_keys(name)
        return name

    def fill_name_field_cyrillic(self):
        name = "Пользователь"
        self.element_is_present(self.locators.DEPARTMENT_NAME_FORM).send_keys(name)
        return name

    def fill_description_field(self):
        person_info = next(generated_person())
        description = person_info.description
        self.element_is_present(self.locators.DESCRIPTION_FORM).send_keys(description)

    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        description = person_info.description
        self.element_is_visible(self.locators.DEPARTMENT_NAME_FORM).send_keys(name)
        self.element_is_visible(self.locators.DESCRIPTION_FORM).send_keys(description)
        return name, description

    def click_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def check_name_fill_form(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DEPARTMENT_NAME_FORM)][0]
        return name

    def check_all_fill_forms(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DEPARTMENT_NAME_FORM)][0]
        description = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DESCRIPTION_FORM)][0]
        return name, description

    def check_perm_list_table(self):
        perms = [x.text for x in self.elements_are_present(self.locators.LIST_PERM_TD)]
        return perms

    def check_form_in_list_by_name(self, name: str):
        list_elements = self.locators.DEPARTMENTS_IN_OVERALL_LIST
        list_elements = (list_elements[0], list_elements[1].replace('*name*', name))
        list_elements = [x.text for x in self.elements_are_present(list_elements)]
        return list_elements

    def click_to_form_by_name(self, name: str):
        temp = self.locators.LIST_DEPARTMENTS_UPDATE_BUTTON
        temp = (temp[0], temp[1].replace('*name*', name))
        self.element_is_present(temp).click()

    def switch_to_role_list(self):
        self.element_is_present(self.locators.LIST_DEPARTMENTS_SWITCH).click()

    def check_alert_name_form(self):
        all_list = self.elements_are_visible(self.locators.NAME_ALERT, timeout=10)
        all_list = [x.text for x in all_list if len(x.text) > 0]
        return all_list
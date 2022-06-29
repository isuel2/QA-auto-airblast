from pages.base_page import BasePage
from locators.admin_users_page_locators import RolesPageLocators
from pages.nav_menu_main_page import MainPageNavMenu
from generator.generator import generated_person


class RolesFormPage(BasePage):
    locators = RolesPageLocators()

    def create_role(self):
        self.element_is_present(self.locators.LIST_ROLE_SWITCH).click()
        self.element_is_present(self.locators.CREATE_ROLE).click()

    def fill_name_field(self):
        person_info = next(generated_person())
        name = person_info.name
        self.element_is_visible(self.locators.ROLE_FORM_NAME).send_keys(name)
        return name

    def fill_name_field_cyrillic(self):
        name = "Пользователь"
        self.element_is_visible(self.locators.ROLE_FORM_NAME).send_keys(name)
        return name

    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        description = person_info.description
        core_limit = person_info.core_limit
        run_job_limit = person_info.run_job_limit
        ram_limit = person_info.ram_limit
        total_core_limit = person_info.total_core_limit
        total_ram_limit = person_info.total_ram_limit
        self.element_is_visible(self.locators.ROLE_FORM_NAME).send_keys(name)
        self.element_is_visible(self.locators.DESCRIPTION_FORM).send_keys(description)
        self.element_is_visible(self.locators.CORE_LIMIT).send_keys(core_limit)
        self.element_is_visible(self.locators.RUNNING_JOB_LIMIT).send_keys(run_job_limit)
        self.element_is_visible(self.locators.RAM_LIMIT).send_keys(ram_limit)
        self.element_is_present(self.locators.TOTAL_CORE_LIMIT).send_keys(total_core_limit)
        self.element_is_visible(self.locators.TOTAL_RAM_LIMIT).send_keys(total_ram_limit)
        return name, description, core_limit, run_job_limit, ram_limit, total_core_limit, total_ram_limit

    def check_name_fill_form(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.ROLE_FORM_NAME)][0]
        return name

    def check_all_fill_forms(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.ROLE_FORM_NAME)][0]
        description = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DESCRIPTION_FORM)][0]
        core_limit = [x.get_attribute('value') for x in self.elements_are_present(self.locators.CORE_LIMIT)][0]
        run_job_limit = [x.get_attribute('value') for x in self.elements_are_present(self.locators.RUNNING_JOB_LIMIT)][
            0]
        ram_limit = [x.get_attribute('value') for x in self.elements_are_present(self.locators.RAM_LIMIT)][0]
        total_core_limit = \
            [x.get_attribute('value') for x in self.elements_are_present(self.locators.TOTAL_CORE_LIMIT)][0]
        total_ram_limit = [x.get_attribute('value') for x in
                           self.elements_are_present(self.locators.TOTAL_RAM_LIMIT)][0]
        return name, description, core_limit, run_job_limit, ram_limit, total_core_limit, total_ram_limit

    def click_submit_button(self):
        self.element_is_present(self.locators.SUBMIT_BUTTON).click()

    def check_form_in_list_by_name(self, name: str):
        list_elements = self.locators.LIST_ROLE
        list_elements = (list_elements[0], list_elements[1].replace('*name*', name))
        list_elements = [x.text for x in self.elements_are_present(list_elements)]
        return list_elements

    def click_to_form_by_name(self, name: str):
        temp = self.locators.LIST_ROLE_UPDATE_BUTTON
        temp = (temp[0], temp[1].replace('*name*', name))
        self.element_is_present(temp).click()

    def switch_to_role_list(self):
        self.element_is_present(self.locators.LIST_ROLE_SWITCH).click()

    def check_alert_name_form(self):
        all_list = self.elements_are_visible(self.locators.NAME_ALERT, timeout=10)
        all_list = [x.text for x in all_list if len(x.text) > 0]
        return all_list

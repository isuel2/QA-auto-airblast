from pages.base_page import BasePage
from locators.admin_page_locators import ImagesPageLocators
from generator.generator import generated_person
from selenium.webdriver.common.action_chains import ActionChains


class ImagesCreatePage(BasePage):
    locators = ImagesPageLocators()

    def create_image(self):
        self.element_is_present(self.locators.CREATE_IMAGE).click()

    def fill_name_field(self):
        person_info = next(generated_person())
        name = person_info.name
        self.element_is_visible(self.locators.NAME_IMAGE_FORM).send_keys(name)
        return name

    def fill_required_fields(self):
        person_info = next(generated_person())
        name = person_info.first_name
        base = person_info.name
        self.element_is_present(self.locators.NAME_IMAGE_FORM).send_keys(name)
        self.element_is_present(self.locators.BASE_IMAGE_FORM).send_keys(base)
        return name, base

    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.first_name
        description = person_info.description
        base = person_info.name
        code_run = "RUN echo $VERSION > image_version"
        self.element_is_present(self.locators.NAME_IMAGE_FORM).send_keys(name)
        self.element_is_present(self.locators.DESCRIPTION_IMAGE_FORM).send_keys(description)
        self.element_is_present(self.locators.BASE_IMAGE_FORM).send_keys(base)
        code_mirror = self.element_is_present(self.locators.CODE_INPUT_FORM)
        actions = ActionChains(self.driver)
        actions.click(code_mirror).perform()
        actions.send_keys(code_run).perform()
        return name, description, base, code_run

    def click_submit_button(self):
        self.element_is_present(self.locators.SUBMIT_BUTTON).click()

    def check_image_in_overall_list(self, name: str):
        list_elements = self.locators.IMAGE_IN_OVERALL_LIST
        list_elements = (list_elements[0], list_elements[1].replace('*name*', str.lower(name)))
        list_elements = [x.text for x in self.elements_are_present(list_elements)]
        return list_elements

    def check_required_fields(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.NAME_IMAGE_FORM)][0]
        base = [x.get_attribute('value') for x in self.elements_are_present(self.locators.BASE_IMAGE_FORM)][0]
        return name, base

    def check_all_fields(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.NAME_IMAGE_FORM)][0]
        description = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DESCRIPTION_IMAGE_FORM)][0]
        base = [x.get_attribute('value') for x in self.elements_are_present(self.locators.BASE_IMAGE_FORM)][0]
        code_run = [x.text for x in self.elements_are_present(self.locators.CODE_INPUT_FORM)][0]
        return name, description, base, code_run

    def build_docker_image(self, name: str):
        temp = self.locators.LIST_IMAGE_BUILD_BUTTON
        temp = (temp[0], temp[1].replace('*name*', name))
        self.element_is_present(temp).click()
        return temp

    def update_image(self, name: str):
        temp = self.locators.LIST_IMAGE_UPDATE_BUTTON
        temp = (temp[0], temp[1].replace('*name*', name))
        self.element_is_present(temp).click()
        return temp

    def access_permissions_image(self, name: str):
        temp = self.locators.LIST_IMAGE_ACCESS_PERMISSIONS
        temp = (temp[0], temp[1].replace('*name*', name))
        self.element_is_present(temp).click()
        return temp

    def check_image_status(self, name: str):
        temp = self.locators.LIST_IMAGE_BUILD_STATUS
        temp = (temp[0], temp[1].replace('*name*', name))
        temp = [x.text for x in self.elements_are_present(temp)]
        return temp


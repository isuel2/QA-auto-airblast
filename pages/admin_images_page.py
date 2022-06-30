from pages.base_page import BasePage
from locators.admin_page_locators import ImagesPageLocators
from generator.generator import generated_person


class ImagesCreatePage(BasePage):
    locators = ImagesPageLocators()

    def create_image(self):
        self.element_is_present(self.locators.CREATE_IMAGE).click()

    def fill_required_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        base = person_info.description
        self.element_is_present(self.locators.NAME_IMAGE_FORM).send_keys(name)
        self.element_is_present(self.locators.BASE_IMAGE_FORM).send_keys(base)
        return name, base

    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        description = person_info.description
        base = person_info.description
        code_run = "RUN echo $VERSION > image_version"
        self.element_is_present(self.locators.NAME_IMAGE_FORM).send_keys(name)
        self.element_is_present(self.locators.DESCRIPTION_IMAGE_FORM).send_keys(description)
        self.element_is_present(self.locators.BASE_IMAGE_FORM).send_keys(base)
        self.element_is_present(self.locators.CODE_INPUT_FORM).send_keys(code_run)
        return name, description, base, code_run

    def check_required_fields(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.NAME_IMAGE_FORM)][0]
        base = [x.get_attribute('value') for x in self.element_is_present(self.locators.BASE_IMAGE_FORM)][0]
        return name, base

    def check_all_fields(self):
        name = [x.get_attribute('value') for x in self.elements_are_present(self.locators.NAME_IMAGE_FORM)][0]
        description = [x.get_attribute('value') for x in self.elements_are_present(self.locators.DESCRIPTION_IMAGE_FORM)][0]
        base = [x.get_attribute('value') for x in self.elements_are_present(self.locators.BASE_IMAGE_FORM)][0]
        code_run = [x.get_attribute('value') for x in self.elements_are_present(self.locators.CODE_INPUT_FORM)][0]
        return name, description, base, code_run

    def build_docker_image(self, name: str):
        temp = self.locators.LIST_IMAGE_BUILD_BUTTON
        temp = (temp[0], temp[1].replace('*name*', name))
        self.element_is_present(temp).click()







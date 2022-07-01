from pages.nav_menu_main_page import MainPageNavMenu
from pages.admin_images_page import ImagesCreatePage
from tests.login_test import TestLoginPage


class TestImageCreate:

    def test_create_image_fill_all_fields(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Images")
        ImagesCreatePage(driver).create_image()
        name, description, base, code_run = ImagesCreatePage(driver).fill_all_fields()
        ImagesCreatePage(driver).click_submit_button()
        ImagesCreatePage(driver).check_image_in_overall_list(name)
        ImagesCreatePage(driver).update_image(str.lower(name))
        output_name, output_description, output_base, output_code_run = ImagesCreatePage(driver).check_all_fields()
        assert str.lower(name) == output_name
        assert description == output_description
        assert base == output_base
        assert code_run == output_code_run.replace("1\n", "")

    def test_create_image_require_fields(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Images")
        ImagesCreatePage(driver).create_image()
        name, base = ImagesCreatePage(driver).fill_required_fields()
        ImagesCreatePage(driver).click_submit_button()
        ImagesCreatePage(driver).check_image_in_overall_list(name)
        ImagesCreatePage(driver).update_image(str.lower(name))
        output_name, output_base = ImagesCreatePage(driver).check_required_fields()
        assert str.lower(name) == output_name
        assert base == output_base

    ###Test: Favorites. all items, build image, status image, cyrillic, empty forms, access permission?????/



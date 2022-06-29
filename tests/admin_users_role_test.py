from pages.nav_menu_main_page import MainPageNavMenu
from pages.admin_users_roles_page import RolesFormPage
from tests.login_test import TestLoginPage


class TestRolePage:

    def test_create_role_all_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesFormPage(driver).create_role()
        name, description, core_limit, run_job_limit, ram_limit, total_core_limit, total_ram_limit \
            = RolesFormPage(driver).fill_all_fields()
        RolesFormPage(driver).click_submit_button()
        RolesFormPage(driver).switch_to_role_list()
        RolesFormPage(driver).check_form_in_list_by_name(name)
        RolesFormPage(driver).click_to_form_by_name(name)
        output_name, output_description, output_core_limit, output_run_job_limit, output_ram_limit, \
        output_total_core_limit, output_total_ram_limit = RolesFormPage(driver).check_all_fill_forms()
        assert name == output_name
        assert description == output_description
        assert str(core_limit) == output_core_limit
        assert str(run_job_limit) == output_run_job_limit
        assert str(ram_limit) == output_ram_limit
        assert str(total_core_limit) == output_total_core_limit
        assert str(total_ram_limit) == output_total_ram_limit

    def test_create_role_required_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesFormPage(driver).create_role()
        name = RolesFormPage(driver).fill_name_field()
        RolesFormPage(driver).click_submit_button()
        RolesFormPage(driver).switch_to_role_list()
        RolesFormPage(driver).check_form_in_list_by_name(name)
        RolesFormPage(driver).click_to_form_by_name(name)
        output_name = RolesFormPage(driver).check_name_fill_form()
        assert name == output_name

    def test_create_role_cyrillic_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesFormPage(driver).create_role()
        RolesFormPage(driver).fill_name_field_cyrillic()
        RolesFormPage(driver).click_submit_button()
        elements = RolesFormPage(driver).check_alert_name_form()
        assert 'Please enter a valid name' in elements

    def test_create_role_empty_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesFormPage(driver).create_role()
        RolesFormPage(driver).click_submit_button()
        elements = RolesFormPage(driver).check_alert_name_form()
        assert 'Enter name!' in elements

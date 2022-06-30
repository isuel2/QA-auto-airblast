from pages.nav_menu_main_page import MainPageNavMenu
from pages.admin_users_roles_page import RolesCreatePage
from tests.login_test import TestLoginPage


class TestRolePage:

    def test_create_role_all_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesCreatePage(driver).create_role()
        name, description, core_limit, run_job_limit, ram_limit, total_core_limit, total_ram_limit \
            = RolesCreatePage(driver).fill_all_fields()
        RolesCreatePage(driver).click_submit_button()
        RolesCreatePage(driver).switch_to_role_list()
        RolesCreatePage(driver).check_form_in_list_by_name(name)
        RolesCreatePage(driver).click_to_form_by_name(name)
        output_name, output_description, output_core_limit, output_run_job_limit, output_ram_limit, \
            output_total_core_limit, output_total_ram_limit = RolesCreatePage(driver).check_all_fill_forms()
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
        RolesCreatePage(driver).create_role()
        name = RolesCreatePage(driver).fill_name_field()
        RolesCreatePage(driver).click_submit_button()
        RolesCreatePage(driver).switch_to_role_list()
        RolesCreatePage(driver).check_form_in_list_by_name(name)
        RolesCreatePage(driver).click_to_form_by_name(name)
        output_name = RolesCreatePage(driver).check_name_fill_form()
        assert name == output_name

    def test_create_role_cyrillic_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesCreatePage(driver).create_role()
        RolesCreatePage(driver).fill_name_field_cyrillic()
        RolesCreatePage(driver).click_submit_button()
        elements = RolesCreatePage(driver).check_alert_name_form()
        assert 'Please enter a valid name' in elements

    def test_create_role_empty_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        RolesCreatePage(driver).create_role()
        RolesCreatePage(driver).click_submit_button()
        elements = RolesCreatePage(driver).check_alert_name_form()
        assert 'Enter name!' in elements


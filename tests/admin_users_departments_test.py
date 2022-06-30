from pages.nav_menu_main_page import MainPageNavMenu
from pages.admin_users_departments_page import DepartmentsCreatePage
from tests.login_test import TestLoginPage


class TestDepartmentPage:

    def test_create_department_all_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        DepartmentsCreatePage(driver).create_department()
        name, description = DepartmentsCreatePage(driver).fill_all_fields()
        DepartmentsCreatePage(driver).click_submit_button()
        DepartmentsCreatePage(driver).switch_to_role_list()
        DepartmentsCreatePage(driver).check_form_in_list_by_name(name)
        DepartmentsCreatePage(driver).click_to_form_by_name(name)
        output_name, output_description = DepartmentsCreatePage(driver).check_all_fill_forms()
        assert name == output_name
        assert description == output_description

    def test_create_department_required_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        DepartmentsCreatePage(driver).create_department()
        name = DepartmentsCreatePage(driver).fill_name_field()
        DepartmentsCreatePage(driver).click_submit_button()
        DepartmentsCreatePage(driver).switch_to_role_list()
        DepartmentsCreatePage(driver).check_form_in_list_by_name(name)
        DepartmentsCreatePage(driver).click_to_form_by_name(name)
        output_name = DepartmentsCreatePage(driver).check_name_fill_form()
        assert name == output_name

    def test_create_department_cyrillic_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        DepartmentsCreatePage(driver).create_department()
        DepartmentsCreatePage(driver).fill_name_field_cyrillic()
        DepartmentsCreatePage(driver).click_submit_button()
        elements = DepartmentsCreatePage(driver).check_alert_name_form()
        assert 'Please enter a valid name' in elements

    def test_create_department_empty_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        DepartmentsCreatePage(driver).create_department()
        DepartmentsCreatePage(driver).click_submit_button()
        elements = DepartmentsCreatePage(driver).check_alert_name_form()
        assert 'Enter name!' in elements
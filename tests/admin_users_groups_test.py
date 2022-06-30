from pages.nav_menu_main_page import MainPageNavMenu
from pages.admin_users_groups_page import GroupsCreatePage
from tests.login_test import TestLoginPage


class TestRolePage:

    def test_create_group_all_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        GroupsCreatePage(driver).create_group()
        name, description = GroupsCreatePage(driver).fill_all_fields()
        GroupsCreatePage(driver).click_submit_button()
        GroupsCreatePage(driver).switch_to_role_list()
        GroupsCreatePage(driver).check_form_in_list_by_name(name)
        GroupsCreatePage(driver).click_to_form_by_name(name)
        output_name, output_description = GroupsCreatePage(driver).check_all_fill_forms()
        assert name == output_name
        assert description == output_description

    def test_create_group_required_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        GroupsCreatePage(driver).create_group()
        name = GroupsCreatePage(driver).fill_name_field()
        GroupsCreatePage(driver).click_submit_button()
        GroupsCreatePage(driver).switch_to_role_list()
        GroupsCreatePage(driver).check_form_in_list_by_name(name)
        GroupsCreatePage(driver).click_to_form_by_name(name)
        output_name = GroupsCreatePage(driver).check_name_fill_form()
        assert name == output_name

    def test_create_group_cyrillic_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        GroupsCreatePage(driver).create_group()
        GroupsCreatePage(driver).fill_name_field_cyrillic()
        GroupsCreatePage(driver).click_submit_button()
        elements = GroupsCreatePage(driver).check_alert_name_form()
        assert 'Please enter a valid name' in elements

    def test_create_group_empty_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        GroupsCreatePage(driver).create_group()
        GroupsCreatePage(driver).click_submit_button()
        elements = GroupsCreatePage(driver).check_alert_name_form()
        assert 'Enter name!' in elements

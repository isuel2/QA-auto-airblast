from pages.nav_menu_main_page import MainPageNavMenu
from pages.admin_users_user_page import UsersCreatePage
from tests.login_test import TestLoginPage


##Добавить тест Активный пользователь, иннактивный пользователь, изменение статуса и проверка в таблице


class TestUserPage:

    def test_create_user_all_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        UsersCreatePage(driver).create_user()
        first_name, last_name, login, password, department, roles, groups \
            = UsersCreatePage(driver).fill_required_fields()
        UsersCreatePage(driver).click_submit_button()
        UsersCreatePage(driver).switch_to_user_list()
        UsersCreatePage(driver).check_form_in_list_by_name(first_name)
        UsersCreatePage(driver).click_to_form_by_name(first_name)
        output_first_name, output_last_name, output_login, output_password, output_department, output_roles, \
        output_groups = UsersCreatePage(driver).check_all_required_form()
        assert first_name == output_first_name
        assert last_name == output_last_name
        assert login == output_login
        assert password == output_password
        assert department == output_department
        assert roles == output_roles
        assert groups == output_groups
        assert 'active' == UsersCreatePage(driver).check_status_user(first_name)

    def test_create_user_required_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        UsersCreatePage(driver).create_user()
        first_name = UsersCreatePage(driver).fill_name_field()
        UsersCreatePage(driver).click_submit_button()
        UsersCreatePage(driver).switch_to_user_list()
        UsersCreatePage(driver).check_form_in_list_by_name(first_name)
        UsersCreatePage(driver).click_to_form_by_name(first_name)
        output_first_name = UsersCreatePage(driver).check_first_name_fill_form()
        assert first_name == output_first_name

    def test_create_user_cyrillic_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        UsersCreatePage(driver).create_user()
        UsersCreatePage(driver).fill_name_field_cyrillic()
        UsersCreatePage(driver).click_submit_button()
        elements = UsersCreatePage(driver).check_alert_name_form()
        assert 'Please enter a valid name' in elements

    def test_create_user_empty_fill_forms(self, driver):
        TestLoginPage().test_login_auth_valid_data(driver)
        MainPageNavMenu(driver).switch_to_admin_menu("Users/Groups")
        UsersCreatePage(driver).create_user()
        UsersCreatePage(driver).click_submit_button()
        elements = UsersCreatePage(driver).check_alert_name_form()
        assert 'Enter name!' in elements


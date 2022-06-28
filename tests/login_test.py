from pages.login_page import LoginPage

valid_login = "gstiblo"
valid_password = "1q2w#E$R"
invalid_login = "asdfggege"
invalid_password = "asdgredg345desw"
invalid_nums_login = "2135435345252"
empty_login = ""
empty_password = ""


class TestLoginPage:

    def test_login_auth_valid_data(self, driver):
        login_page = LoginPage(driver, 'https://bdas-utility-01.bdpak.frontier.kz:7002/')
        login_page.open()
        login_page.enter_login_and_password(valid_login, valid_password)
        login_page.click_on_the_button()
        title_login = login_page.check_navigation_bar_title_login(valid_login)
        assert valid_login in title_login, "the full name does not match"

    def test_login_auth_invalid_data(self, driver):
        login_page = LoginPage(driver, 'https://bdas-utility-01.bdpak.frontier.kz:7002/')
        login_page.open()
        login_page.enter_login_and_password(invalid_login, invalid_password)
        login_page.click_on_the_button()
        elements = login_page.check_login_page_title_menu()
        assert 'Логин' in elements

    def test_login_auth_numbers_login_data(self, driver):
        login_page = LoginPage(driver, 'https://bdas-utility-01.bdpak.frontier.kz:7002/')
        login_page.open()
        login_page.enter_login_and_password(invalid_nums_login, valid_password)
        login_page.click_on_the_button()
        elements = login_page.check_login_page_title_menu()
        assert 'Логин' in elements

    def test_login_auth_empty_login_valid_password_data(self, driver):
        login_page = LoginPage(driver, 'https://bdas-utility-01.bdpak.frontier.kz:7002/')
        login_page.open()
        login_page.enter_login_and_password(empty_login, valid_password)
        login_page.click_on_the_button()
        elements = login_page.check_alert_insert_login()
        assert 'Введите логин' in elements

    def test_login_auth_valid_login_empty_password_data(self, driver):
        login_page = LoginPage(driver, 'https://bdas-utility-01.bdpak.frontier.kz:7002/')
        login_page.open()
        login_page.enter_login_and_password(valid_login, empty_password)
        login_page.click_on_the_button()
        elements = login_page.check_alert_insert_password()
        assert 'Введите пароль' in elements




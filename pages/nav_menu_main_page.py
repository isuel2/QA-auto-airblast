from locators.nav_menu_locators import NavMenuLocators
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageNavMenu(BasePage):
    locators = NavMenuLocators()
    login_locators = LoginPageLocators()

    def switch_to_jobs_menu(self, href):
        jobs_menu = self.element_is_visible(self.locators.JOBS_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(jobs_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_datasets_menu(self, href):
        datasets_menu = self.element_is_visible(self.locators.DATASETS_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(datasets_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_analytics_menu(self, href):
        analytics_menu = self.element_is_visible(self.locators.ANALYTICS_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(analytics_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_directories_menu(self, href):
        directories_menu = self.element_is_visible(self.locators.DIRECTORIES_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(directories_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_admin_menu(self, href):
        admin_menu = self.element_is_visible(self.locators.ADMIN_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(admin_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_help_menu(self, href):
        help_menu = self.element_is_visible(self.locators.HELP_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(help_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_inner_task_menu(self, href):
        inner_task_menu = self.element_is_visible(self.locators.INNER_TASK_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(inner_task_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_favorites_menu(self, href):
        favorites_menu = self.element_is_visible(self.locators.FAVORITES_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(favorites_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_alerts_menu(self, href):
        alerts_menu = self.element_is_visible(self.locators.ALERTS_MENU)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(alerts_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def switch_to_login_menu(self, href):
        login_menu = self.element_is_visible(self.login_locators.NAVIGATION_BAR)
        hidden_submenu = self.driver.find_element(By.XPATH, f"//a[normalize-space()='{href}']")
        actions = self.action_move_to_element(login_menu)
        actions.click(hidden_submenu)
        actions.perform()

    def check_alert_users_groups_tablist(self):
        all_lists = self.element_is_visible(self.locators.INSIDE_USERS_GROUPS_MODULE)
        all_lists = [x.text for x in all_lists if len(x.text) > 0]
        return all_lists

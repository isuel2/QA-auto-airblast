from selenium.webdriver.common.by import By


class NavMenuLocators:
    JOBS_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='Jobs']")
    DATASETS_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='Datasets']")
    ANALYTICS_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='Analytics']")
    DIRECTORIES_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='Datasets']")
    ADMIN_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='Admin']")
    HELP_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='Help']")
    INNER_TASK_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[@href='/inner-tasks']")
    FAVORITES_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[@href='/favorites']")
    ALERTS_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[@href='/alerts']")
    LOGIN_MENU = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='gstiblo']")
    INSIDE_USERS_GROUPS_MODULE = (By.XPATH, "//div[@role='tablist']")
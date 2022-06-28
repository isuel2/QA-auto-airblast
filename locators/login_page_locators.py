from selenium.webdriver.common.by import By


class LoginPageLocators:
    #login form
    LOGIN_FORM = (By.ID, "username")
    PASSWORD_FORM = (By.ID, "password")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    #page after login
    NAVIGATION_BAR = (By.XPATH, "//*[@class='ant-menu-submenu-title']//*[text()='*login*']")
    TITLE_LOGIN_PASSWORD_FORM = (By.XPATH, "//*[@class='ant-card-body']//*[@title='Логин']")
    TITLE_LOGIN_PASSWORD_FORM_ALERT_INSERT_PASSWORD = (By.XPATH, "//*[@class='ant-col ant-col-16 "
                                                                 "ant-form-item-control']//*["
                                                                 "@class='ant-form-item-explain-error']")
    TITLE_LOGIN_PASSWORD_FORM_ALERT_INSERT_LOGIN = (By.XPATH, "//*[@class='ant-col ant-col-16 "
                                                              "ant-form-item-control']//*["
                                                              "@class='ant-form-item-explain-error']")

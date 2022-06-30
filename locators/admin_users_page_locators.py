from selenium.webdriver.common.by import By


class UsersPageLocators:
    CREATE_USER = (By.XPATH, "//a[normalize-space()='Create user']")
    FIRST_NAME_FORM = (By.ID, "userForm_first_name")
    LAST_NAME_FORM = (By.ID, "userForm_last_name")
    LOGIN_FORM = (By.ID, "userForm_username")
    PASSWORD_FORM = (By.ID, "userForm_password")
    DEPARTMENTS_FORM = (By.ID, "userForm_department_id")
    ROLES_FORM = (By.ID, "userForm_roles")
    GROUPS_FORM = (By.ID, "userForm_groups")
    EMAIL_FORM = (By.ID, "userForm_email")
    PHONE_FORM = (By.ID, "userForm_phone")
    TELEGRAM_FORM = (By.ID, "userForm_tg_id")
    TYPE_PERMISSION = (By.ID, "type")
    ACTION_PERMISSION = (By.ID, "action")
    CREATED_BY_PERMISSION = (By.ID, "created")
    LIST_PERMISSIONS_IN_FORM = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-tbody']")
    LIST_PERM_TD = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-content']//following::td")
    SUBMIT_PERMISSIONS = (By.XPATH, "(//button[@type='submit'])[1]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@form='roleForm']//span")
    LIST_USER_SWITCH = (By.ID, "rc-tabs-0-tab-users")
    LIST_USER = (By.XPATH, "*//tbody//*[text()='*first-name*']")
    LIST_USER_UPDATE_BUTTON = (By.XPATH, "*//td//span[text()='*first-name*']//following::a")
    LIST_USER_DELETE_FROM_LIST = (By.XPATH, "*//td//span[text()='first-name*']//following::button[2]")
    LIST_USER_DELETE_BUTTON = (By.XPATH, "//*[@class='ant-popover-inner-content']//following::button[2]")
    MODAL_WINDOW_ROLE = (By.XPATH, "//*[@role='document']")
    MODAL_WINDOW_ROLE_INPUTS_LIMITS = (
        By.XPATH, "//*[@class='ant-modal']//*[@class='ant-input-number-input']")


class DepartmentsPageLocators:
    CREATE_DEPARTMENT = (By.XPATH, "//a[normalize-space()='Create department']")
    DEPARTMENT_NAME_FORM = (By.ID, "departmentForm_name")
    DESCRIPTION_FORM = (By.ID, "departmentForm_description")
    TYPE_PERMISSION = (By.ID, "type")
    ACTION_PERMISSION = (By.ID, "action")
    CREATED_BY_PERMISSION = (By.ID, "created")
    LIST_PERMISSIONS_IN_FORM = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-tbody']")
    LIST_PERM_TD = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-content']//following::td")
    SUBMIT_PERMISSIONS = (By.XPATH, "(//button[@type='submit'])[1]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@form='departmentForm']//span")
    LIST_DEPARTMENTS_SWITCH = (By.ID, "rc-tabs-0-tab-departments")
    LIST_DEPARTMENTS = (By.XPATH, "*//tbody//*[text()='*name*']")
    LIST_DEPARTMENTS_UPDATE_BUTTON = (By.XPATH, "*//td//span[text()='*name*']//following::a")
    LIST_DEPARTMENT_DELETE_FROM_LIST = (By.XPATH, "*//td//span[text()='*name*']//following::button[2]")
    LIST_DEPARTMENT_DELETE_BUTTON = (By.XPATH, "//*[@class='ant-popover-inner-content']//following::button[2]")
    MODAL_WINDOW_DEPARTMENT = (By.XPATH, "//*[@role='document']")
    MODAL_WINDOW_ROLE_INPUTS_LIMITS = (
        By.XPATH, "//*[@class='ant-modal']//*[@class='ant-input-number-input']")
    NAME_ALERT = (By.XPATH, "//*[@class='ant-col ant-col-14 "
                            "ant-form-item-control']//*["
                            "@class='ant-form-item-explain-error']")


class GroupsPageLocators:
    CREATE_GROUP = (By.XPATH, "//a[normalize-space()='Create group']")
    GROUP_NAME_FORM = (By.ID, "groupForm_name")
    DESCRIPTION_FORM = (By.ID, "groupForm_description")
    TYPE_PERMISSION = (By.ID, "type")
    ACTION_PERMISSION = (By.ID, "action")
    CREATED_BY_PERMISSION = (By.ID, "created")
    LIST_PERMISSIONS_IN_FORM = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-tbody']")
    LIST_PERM_TD = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-content']//following::td")
    SUBMIT_PERMISSIONS = (By.XPATH, "(//button[@type='submit'])[1]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@form='groupForm']//span")
    LIST_GROUP_SWITCH = (By.ID, "rc-tabs-0-tab-groups")
    LIST_GROUP = (By.XPATH, "*//tbody//*[text()='*name*']")
    LIST_GROUP_UPDATE_BUTTON = (By.XPATH, "*//td//span[text()='*name*']//following::a")
    LIST_GROUP_DELETE_FROM_LIST = (By.XPATH, "*//td//span[text()='*name*']//following::button[2]")
    LIST_GROUP_DELETE_BUTTON = (By.XPATH, "//*[@class='ant-popover-inner-content']//following::button[2]")
    MODAL_WINDOW_ROLE = (By.XPATH, "//*[@role='document']")
    MODAL_WINDOW_ROLE_INPUTS_LIMITS = (
        By.XPATH, "//*[@class='ant-modal']//*[@class='ant-input-number-input']")
    NAME_ALERT = (By.XPATH, "//*[@class='ant-col ant-col-14 "
                            "ant-form-item-control']//*["
                            "@class='ant-form-item-explain-error']")


# class JobsDatasetsPageLocators:

class RolesPageLocators:
    CREATE_ROLE = (By.XPATH, "//a[normalize-space()='Create role']")
    ROLE_NAME_FORM = (By.ID, "roleForm_name")
    DESCRIPTION_FORM = (By.ID, "roleForm_description")
    CORE_LIMIT = (By.ID, "roleForm_core_limit")
    RUNNING_JOB_LIMIT = (By.ID, "roleForm_running_job_limit")
    RAM_LIMIT = (By.ID, "roleForm_ram_limit")
    TOTAL_CORE_LIMIT = (By.ID, "roleForm_total_core_limit")
    TOTAL_RAM_LIMIT = (By.ID, "roleForm_total_ram_limit")
    TYPE_PERMISSION = (By.ID, "type")
    ACTION_PERMISSION = (By.ID, "action")
    CREATED_BY_PERMISSION = (By.ID, "created")
    LIST_PERMISSIONS_IN_FORM = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-tbody']")
    LIST_PERM_TD = (By.XPATH, "//*[@class='ant-modal']//*[@class='ant-table-content']//following::td")
    SUBMIT_PERMISSIONS = (By.XPATH, "(//button[@type='submit'])[1]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@form='roleForm']//span")
    LIST_ROLE_SWITCH = (By.ID, "rc-tabs-0-tab-roles")
    LIST_ROLE = (By.XPATH, "*//tbody//*[text()='*name*']")
    LIST_ROLE_UPDATE_BUTTON = (By.XPATH, "*//td//span[text()='*name*']//following::a")
    LIST_ROLE_DELETE_FROM_LIST = (By.XPATH, "*//td//span[text()='*name*']//following::button[2]")
    LIST_ROLE_DELETE_BUTTON = (By.XPATH, "//*[@class='ant-popover-inner-content']//following::button[2]")
    MODAL_WINDOW_ROLE = (By.XPATH, "//*[@role='document']")
    MODAL_WINDOW_ROLE_INPUTS_LIMITS = (
        By.XPATH, "//*[@class='ant-modal']//*[@class='ant-input-number-input']")
    NAME_ALERT = (By.XPATH, "//*[@class='ant-col ant-col-16 "
                            "ant-form-item-control']//*["
                            "@class='ant-form-item-explain-error']")

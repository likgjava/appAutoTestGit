from itcast.autotest.ikcrm.page.base import BasePage


class LoginPage(BasePage):
    """
    登录页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_user_name_element(self):
        return self.driver.find_element_by_id('com.vcooline.aike:id/login_username_edit')

    def find_password_element(self):
        return self.driver.find_element_by_id('com.vcooline.aike:id/login_password_edit')

    def find_login_but_element(self):
        return self.driver.find_element_by_id('com.vcooline.aike:id/button_login')


class LoginHandle:
    """
    登录页面-操作层
    """

    def __init__(self):
        self.loginPage = LoginPage()

    def set_user_name(self, user_name):
        self.loginPage.find_user_name_element().clear().send_keys(user_name)

    def set_password(self, password):
        self.loginPage.find_password_element().clear().send_keys(password)

    def click_login_but(self):
        self.loginPage.find_login_but_element().click()


class LoginProxy:
    """
    登录页面-业务层
    """

    def __init__(self):
        self.loginHandle = LoginHandle()

    def login(self, user_name, password):
        self.loginHandle.set_user_name(user_name)
        self.loginHandle.set_password(password)
        self.loginHandle.click_login_but()

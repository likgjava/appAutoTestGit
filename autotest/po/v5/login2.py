from selenium.webdriver.common.by import By

from autotest.po.v5.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """
    登录页面-对象库层
    """

    def __init__(self):
        super().__init__()

        self.user_name = (By.ID, "net.csdn.csdnplus:id/editTextUserName")
        self.password = (By.ID, "net.csdn.csdnplus:id/password")
        self.login_btn = (By.ID, "net.csdn.csdnplus:id/csdnsign_in_button")

    def find_user_name(self):
        return self.find_element(self.user_name)

    def find_password(self):
        return self.find_element(self.password)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    """
    登录页面-操作层
    """

    def __init__(self):
        self.login_page = LoginPage()

    def input_user_name(self, user_name):
        self.send_keys(self.login_page.find_user_name(), user_name)

    def input_password(self, password):
        self.send_keys(self.login_page.find_password(), password)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:
    """
    登录页面-业务层
    """

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, user_name, password):
        self.login_handle.input_user_name(user_name)
        self.login_handle.input_password(password)
        self.login_handle.click_login_btn()

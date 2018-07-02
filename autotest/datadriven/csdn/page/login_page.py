from itcast.autotest.datadriven.csdn.page.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """
    登录页面-对象库层
    """

    def __init__(self):
        super().__init__()

        self.user_name = "net.csdn.csdnplus:id/editTextUserName"
        self.password = "net.csdn.csdnplus:id/password"
        self.login_button = "net.csdn.csdnplus:id/csdnsign_in_button"

    def find_user_name_element(self):
        return self.find_element_by_id(self.user_name)

    def find_password_element(self):
        return self.find_element_by_id(self.password)

    def find_login_btn_element(self):
        return self.find_element_by_id(self.login_button)


class LoginHandle(BaseHandle):
    """
    登录页面-操作层
    """

    def __init__(self):
        self.loginPage = LoginPage()

    def set_user_name(self, user_name):
        self.send_keys(self.loginPage.find_user_name_element(), user_name)

    def set_password(self, password):
        self.send_keys(self.loginPage.find_password_element(), password)

    def click_login_btn(self):
        self.loginPage.find_login_btn_element().click()


class LoginProxy:
    """
    登录页面-业务层
    """

    def __init__(self):
        self.loginHandle = LoginHandle()

    def login(self, user_name, password):
        self.loginHandle.set_user_name(user_name)
        self.loginHandle.set_password(password)
        self.loginHandle.click_login_btn()

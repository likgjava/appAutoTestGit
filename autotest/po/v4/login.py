from autotest.po.utils import DriverUtil


class LoginPage:
    """
    登录页面-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()

        self.user_name = None
        self.password = None
        self.login_btn = None

    def find_user_name(self):
        return self.driver.find_element_by_id("net.csdn.csdnplus:id/editTextUserName")

    def find_password(self):
        return self.driver.find_element_by_id("net.csdn.csdnplus:id/password")

    def find_login_btn(self):
        return self.driver.find_element_by_id("net.csdn.csdnplus:id/csdnsign_in_button")


class LoginHandle:
    """
    登录页面-操作层
    """

    def __init__(self):
        self.login_page = LoginPage()

    def input_user_name(self, user_name):
        self.login_page.find_user_name().send_keys(user_name)

    def input_password(self, password):
        self.login_page.find_password().send_keys(password)

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

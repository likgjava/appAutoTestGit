from itcast.autotest.po.utils import DriverUtil


class LoginPage:
    """
    登录页面-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.driver.implicitly_wait(10)

        self.user_name = "net.csdn.csdnplus:id/editTextUserName"
        self.password = "net.csdn.csdnplus:id/password"
        self.login_button = "net.csdn.csdnplus:id/csdnsign_in_button"

    def find_user_name_element(self):
        return self.driver.find_element_by_id(self.user_name)

    def find_password_element(self):
        return self.driver.find_element_by_id(self.password)

    def find_login_btn_element(self):
        return self.driver.find_element_by_id(self.login_button)


class LoginHandle:
    """
    登录页面-操作层
    """

    def __init__(self):
        self.loginPage = LoginPage()

    def set_user_name(self, user_name):
        self.loginPage.find_user_name_element().send_keys(user_name)

    def set_password(self, password):
        self.loginPage.find_password_element().send_keys(password)

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

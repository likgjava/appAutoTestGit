from itcast.autotest.ikcrm.page.base import BasePage
from itcast.autotest.ikcrm.page.select_read_over import SelectReadOverProxy


class AddCuePage(BasePage):
    """
    新增线索页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_name_element(self):
        """姓名输入框"""
        xpath = '//android.widget.EditText[@text="姓名"]'
        return self.driver.find_element_by_xpath(xpath)

    def find_company_name_element(self):
        """公司名称输入框"""
        xpath = '//android.widget.EditText[@text="公司名称"]'
        return self.driver.find_element_by_xpath(xpath)

    def find_phone_element(self):
        """电话输入框"""
        xpath = '//android.widget.EditText[@text="电话"]'
        return self.driver.find_element_by_xpath(xpath)

    def find_save_but_element(self):
        """保存按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/tv_crm_add')


class AddCueHandle:
    """
    新增线索页面-操作层
    """

    def __init__(self):
        self.addCuePage = AddCuePage()
        self.selectReadOverProxy = SelectReadOverProxy()

    def set_name(self, name):
        self.addCuePage.find_name_element().send_keys(name)

    def set_company_name(self, company_name):
        self.addCuePage.find_company_name_element().send_keys(company_name)

    def set_phone(self, phone):
        self.addCuePage.find_phone_element().send_keys(phone)

    def click_save_but(self):
        self.addCuePage.find_save_but_element().click()

    def is_save_success(self):
        element = self.addCuePage.get_toast('保存成功')
        return element is not None


class AddCueProxy:
    """
    新增线索页面-业务层
    """

    def __init__(self):
        self.addCueHandle = AddCueHandle()

    def add_cue(self, name, company_name, phone):
        """新增线索"""
        self.addCueHandle.set_name(name)
        self.addCueHandle.set_company_name(company_name)
        self.addCueHandle.set_phone(phone)
        self.addCueHandle.click_save_but()
        # 验证是否提交成功
        is_success = self.addCueHandle.is_save_success()
        print('is_success=', is_success)
        assert is_success

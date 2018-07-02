import time

from itcast.autotest.ikcrm.page.base import BasePage


class SelectReadOverPage(BasePage):
    """
    选择批阅人页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_search_element(self):
        return self.driver.find_element_by_id('com.vcooline.aike:id/edit_search_name')

    def find_first_element(self):
        xpath = '//*[@resource-id="com.vcooline.aike:id/user_list"]//android.widget.LinearLayout[@index=0]//android.widget.RelativeLayout[@index=1]'
        return self.driver.find_element_by_xpath(xpath)

    def find_read_over_element(self, name):
        xpath = '//android.widget.TextView[@resource-id="com.vcooline.aike:id/name"][@text="{}"]'.format(name)
        return self.driver.find_element_by_xpath(xpath)


class SelectReadOverHandle:
    """
    选择批阅人页面-操作层
    """

    def __init__(self):
        self.selectReadOverPage = SelectReadOverPage()

    def set_search_kw(self, kw):
        self.selectReadOverPage.find_search_element().send_keys(kw)

    def select_first_read_over(self):
        self.selectReadOverPage.find_first_element().click()


class SelectReadOverProxy:
    """
    选择批阅人页面-业务层
    """

    def __init__(self):
        self.selectReadOverHandle = SelectReadOverHandle()

    def select_read_over(self, read_over):
        self.selectReadOverHandle.set_search_kw(read_over)

        time.sleep(3)

        self.selectReadOverHandle.select_first_read_over()

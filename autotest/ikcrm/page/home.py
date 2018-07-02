from itcast.autotest.ikcrm.page.base import BasePage
from itcast.autotest.ikcrm.utils import DriverUtil


class HomePage(BasePage):
    """
    主页页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_quick_but_element(self):
        """快捷功能按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/ivFeatures')

    def find_work_but_element(self):
        """工作按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/rbCRMLayout')

    def find_cancel_but_element(self):
        """提示框取消按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/btn_neg')

    def find_try_out_but_element(self):
        """试用提示框确认按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/btn_pos')


class HomeHandle:
    """
    主页页面-操作层
    """

    def __init__(self):
        self.homePage = HomePage()

    def click_cancel_but(self):
        """点击提示框取消按钮"""
        self.homePage.find_cancel_but_element().click()

    def click_try_out_but(self):
        """点击试用提示框确认按钮"""
        self.homePage.find_try_out_but_element().click()

    def click_work_but(self):
        """点击工作按钮"""
        self.homePage.find_work_but_element().click()

    def click_quick_but(self):
        """点击快捷功能按钮"""
        self.homePage.find_quick_but_element().click()


class HomeProxy:
    """
    主页页面-业务层
    """

    def __init__(self):
        self.homeHandle = HomeHandle()

    def deal_tip(self):
        """处理提示框"""
        try:
            self.homeHandle.click_try_out_but()
        except:
            print('not find tip window.')

        try:
            self.homeHandle.click_cancel_but()
        except:
            print('not find tip window.')

    def entry_quick_page(self):
        """进入快捷功能页面"""
        # 如果有提示框，则先关闭提示框
        self.deal_tip()

        self.homeHandle.click_quick_but()

    def entry_work_page(self):
        """进入工作页面"""
        # 如果有提示框，则先关闭提示框
        self.deal_tip()

        self.homeHandle.click_work_but()

    def switch_to_home_page(self):
        """切换到主页"""
        DriverUtil.get_driver().start_activity('com.vcooline.aike', '.activity.MainActivity')

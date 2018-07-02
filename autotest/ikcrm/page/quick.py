from selenium.webdriver.common.by import By

from itcast.autotest.ikcrm.page.base import BasePage


class QuickPage(BasePage):
    """
    快捷功能页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_guide_page_element(self):
        """引导页"""
        xpath = '//android.widget.RelativeLayout'
        id = 'com.vcooline.aike:id/show_my_list'
        return self.driver.find_element_by_id(id)

    def find_write_report_but_element(self):
        """写日报按钮"""
        xpath = '//android.widget.TextView[@text="写日报"]'
        return self.driver.find_element_by_xpath(xpath)

    def find_add_cue_but_element(self):
        """新增线索按钮"""
        xpath = '//android.widget.TextView[@text="新增线索"]'

        try:
            # 上滑查找
            return self.find_element_by_swipe_up(By.XPATH, xpath)
        except:
            # 左滑查找
            return self.find_element_by_swipe_left(By.XPATH, xpath)


class QuickHandle:
    """
    快捷功能页面-操作层
    """

    def __init__(self):
        self.quickPage = QuickPage()

    def click_guide_page(self):
        """点击引导页"""
        self.quickPage.find_guide_page_element().click()

    def click_write_report_but(self):
        """点击写日报按钮"""
        self.quickPage.find_write_report_but_element().click()

    def click_add_cue_but(self):
        """点击新增线索按钮"""
        self.quickPage.find_add_cue_but_element().click()


class QuickProxy:
    """
    快捷功能页面-业务层
    """

    def __init__(self):
        self.quickHandle = QuickHandle()

    def close_guide_page(self):
        """关闭引导页"""
        for i in range(2):
            try:
                self.quickHandle.click_guide_page()
            except Exception as e:
                print('close guide page error')

    def entry_write_report_page(self):
        """进入写日报页面"""
        self.quickHandle.click_write_report_but()

    def entry_add_cue_page(self):
        """进入新增线索页面"""
        self.quickHandle.click_add_cue_but()

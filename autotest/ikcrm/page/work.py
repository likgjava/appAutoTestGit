from selenium.webdriver.common.by import By

from itcast.autotest.ikcrm.page.base import BasePage


class WorkPage(BasePage):
    """
    工作页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_work_report_element(self):
        return self.find_element_by_swipe_up(By.XPATH, '//android.widget.TextView[@text="工作报告"]')

    def find_cue_element(self):
        return self.find_element_by_swipe_up(By.XPATH, '//android.widget.TextView[@text="线索"]')


class WorkHandle:
    """
    工作页面-操作层
    """

    def __init__(self):
        self.workPage = WorkPage()

    def click_work_report(self):
        self.workPage.find_work_report_element().click()

    def click_cue(self):
        self.workPage.find_cue_element().click()


class WorkProxy:
    """
    工作页面-业务层
    """

    def __init__(self):
        self.workHandle = WorkHandle()

    def entry_work_report_page(self):
        self.workHandle.click_work_report()

    def entry_cue_page(self):
        self.workHandle.click_cue()

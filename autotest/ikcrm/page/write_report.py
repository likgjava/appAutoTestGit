from selenium.webdriver.common.by import By

from itcast.autotest.ikcrm.page.base import BasePage
from itcast.autotest.ikcrm.page.select_read_over import SelectReadOverProxy


class WriteReportPage(BasePage):
    """
    写日报页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_summary_element(self):
        """总结输入框"""
        xpath = '//android.widget.TextView[@text="总结"]/following-sibling::android.widget.EditText'
        return self.driver.find_element_by_xpath(xpath)

    def find_plan_element(self):
        """计划输入框"""
        xpath = '//android.widget.TextView[@text="计划"]/following-sibling::android.widget.EditText'
        return self.driver.find_element_by_xpath(xpath)

    def find_read_over_element(self):
        """选择批阅人按钮"""
        xpath = '//android.widget.TextView[@text="批阅人"]'
        return self.find_element_by_swipe_up(By.XPATH, xpath)

    def find_submit_but_element(self):
        """提交按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/tv_crm_add')


class WriteReportHandle:
    """
    写日报页面-操作层
    """

    def __init__(self):
        self.writeReportPage = WriteReportPage()
        self.selectReadOverProxy = SelectReadOverProxy()

    def set_summary(self, summary):
        element = self.writeReportPage.find_summary_element()
        element.clear()
        element.send_keys(summary)

    def set_plan(self, plan):
        self.writeReportPage.find_plan_element().send_keys(plan)

    def select_read_over(self, read_over):
        """选择批阅人"""
        self.writeReportPage.find_read_over_element().click()
        self.selectReadOverProxy.select_read_over(read_over)

    def click_submit_but(self):
        self.writeReportPage.find_submit_but_element().click()

    def is_submit_success(self):
        element = self.writeReportPage.get_toast('提交成功')
        return element is not None


class WriteReportProxy:
    """
    写日报页面-业务层
    """

    def __init__(self):
        self.writeReportHandle = WriteReportHandle()

    def write_report(self, summary, plan, read_over):
        """写日报"""
        if summary is not "":
            self.writeReportHandle.set_summary(summary)
        if plan is not "":
            self.writeReportHandle.set_plan(plan)
        if read_over is not "":
            self.writeReportHandle.select_read_over(read_over)
        self.writeReportHandle.click_submit_but()


from itcast.autotest.ikcrm.page.base import BasePage


class WorkReportPage(BasePage):
    """
    工作报告页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_add_but_element(self):
        return self.driver.find_element_by_id('com.vcooline.aike:id/tv_crm_add')


class WorkReportHandle:
    """
    工作报告页面-操作层
    """

    def __init__(self):
        self.workReportPage = WorkReportPage()

    def click_add_but(self):
        self.workReportPage.find_add_but_element().click()


class WorkReportProxy:
    """
    工作报告页面-业务层
    """

    def __init__(self):
        self.workReportHandle = WorkReportHandle()

    def entry_add_report_page(self):
        self.workReportHandle.click_add_but()

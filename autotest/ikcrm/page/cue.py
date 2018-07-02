from itcast.autotest.ikcrm.page.base import BasePage
from itcast.autotest.ikcrm.page.select_read_over import SelectReadOverProxy


class CuePage(BasePage):
    """
    线索页面-对象库层
    """

    def __init__(self):
        super().__init__()

    def find_add_but_element(self):
        """新增按钮"""
        return self.driver.find_element_by_id('com.vcooline.aike:id/tv_crm_add')


class CueHandle:
    """
    线索页面-操作层
    """

    def __init__(self):
        self.cuePage = CuePage()

    def click_add_but(self):
        self.cuePage.find_add_but_element().click()


class CueProxy:
    """
    线索页面-业务层
    """

    def __init__(self):
        self.cueHandle = CueHandle()

    def entry_add_cue_page(self):
        """进入新增线索页面"""
        self.cueHandle.click_add_but()

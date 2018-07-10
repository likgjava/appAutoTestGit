from autotest.po.utils import DriverUtil


class BasePage(object):
    """
    基础-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        return self.driver.find_element(location[0], location[1])


class BaseHandle(object):
    """
    基础-操作层
    """

    def send_keys(self, element, text):
        """
        在文本框中输入内容，输入前先清空
        :param element: 文本框元素
        :param text: 输入内容
        """
        element.clear()
        element.send_keys(text)

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from itcast.autotest.ikcrm.utils import DriverUtil


class BasePage:

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def _swipe(self):
        self.driver.swipe()

    def get_window_size(self):
        window = self.driver.get_window_size()
        x = window['width']
        y = window['height']
        return x, y

    def swipe_up(self):
        """
        向上滑动屏幕
        :return: 是否滑动成功[True:滑动成功; False:滑动失败]
        """
        x, y = self.get_window_size()
        start_x = 0.5 * x
        start_y = 0.75 * y
        end_x = 0.5 * x
        end_y = 0.25 * y
        old = self.driver.page_source
        self.driver.swipe(start_x, start_y, end_x, end_y, 500)
        new = self.driver.page_source
        return old != new

    def swipe_left(self):
        """
        向左滑动屏幕
        :return: 是否滑动成功[True:滑动成功; False:滑动失败]
        """
        x, y = self.get_window_size()
        start_x = 0.75 * x
        start_y = 0.5 * y
        end_x = 0.25 * x
        end_y = 0.5 * y
        old = self.driver.page_source
        self.driver.swipe(start_x, start_y, end_x, end_y, 500)
        new = self.driver.page_source
        return old != new

    def find_element_by_swipe_up(self, by, value):
        """
        向上滑动屏幕查找元素，如果滑动到底部还没有找到元素则抛异常
        :param by: 查找方式
        :param value: 查找内容
        :return: 查找到的元素
        """
        print('find_element_by_swipe_up...')
        while True:
            try:
                return self.driver.find_element(by, value)
            except WebDriverException:
                swipe_success = self.swipe_up()
                if not swipe_success:
                    print('滑到底了也没找到元素！！！')
                    raise

    def find_element_by_swipe_left(self, by, value):
        """
        向左滑动屏幕查找元素，如果滑动到最右边的屏幕还没有找到元素则抛异常
        :param by: 查找方式
        :param value: 查找内容
        :return: 查找到的元素
        """
        print('find_element_by_swipe_left...')
        while True:
            try:
                return self.driver.find_element(by, value)
            except WebDriverException:
                swipe_success = self.swipe_left()
                if not swipe_success:
                    print('滑到最右边了也没找到元素！！！')
                    raise

    def get_toast(self, toast):
        element = None
        try:
            xpath = ".//*[contains(@text,'{}')]".format(toast)
            element = WebDriverWait(self.driver, 10, 0.01).until(lambda x: x.find_element_by_xpath(xpath))
        except:
            print('not find toast={}'.format(toast))
        return element

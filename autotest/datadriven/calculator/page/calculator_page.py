from selenium.webdriver.common.by import By

from autotest.datadriven.calculator.utils import DriverUtil


class CalculatorPage:
    """
    计算器页面-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()

        # 数字按钮
        self.digit_btn = (By.ID, "com.android.calculator2:id/digit_{}")
        # 加法按钮
        self.add_btn = (By.ID, "com.android.calculator2:id/op_add")
        # 等号按钮
        self.eq_btn = (By.ID, "com.android.calculator2:id/eq")
        # 计算结果
        self.result = (By.ID, "com.android.calculator2:id/formula")

    def find_digit_btn(self, digit):
        location = (self.digit_btn[0], self.digit_btn[1].format(digit))
        return self.driver.find_element(*location)

    def find_add_btn(self):
        return self.driver.find_element(*self.add_btn)

    def find_eq_btn(self):
        return self.driver.find_element(*self.eq_btn)

    def find_result(self):
        return self.driver.find_element(*self.result)


class CalculatorHandle:
    """
    计算器页面-操作层
    """

    def __init__(self):
        self.calculatorPage = CalculatorPage()

    def click_digit_button(self, digit):
        self.calculatorPage.find_digit_btn(digit).click()

    def click_add_button(self):
        self.calculatorPage.find_add_btn().click()

    def click_eq_button(self):
        self.calculatorPage.find_eq_btn().click()

    def get_result_text(self):
        return self.calculatorPage.find_result().text

    def input_numbers(self, numbers):
        for num in numbers:
            self.click_digit_button(num)


class CalculatorProxy:
    """
    计算器页面-业务层
    """

    def __init__(self):
        self.calculatorHandle = CalculatorHandle()

    def add(self, num1, num2):
        self.calculatorHandle.input_numbers(num1)
        self.calculatorHandle.click_add_button()
        self.calculatorHandle.input_numbers(num2)
        self.calculatorHandle.click_eq_button()

    def get_result(self):
        return self.calculatorHandle.get_result_text()

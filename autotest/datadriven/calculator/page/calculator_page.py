from itcast.autotest.datadriven.calculator.page.base_page import BasePage, BaseHandle


class CalculatorPage(BasePage):
    """
    计算器页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 数字按钮
        self.digit_button = "com.android.calculator2:id/digit_{}"
        # 加法按钮
        self.add_button = "com.android.calculator2:id/op_add"
        # 等号按钮
        self.eq_button = "com.android.calculator2:id/eq"
        # 计算结果
        self.result = "com.android.calculator2:id/formula"

    def find_digit_button_element(self, digit):
        return self.find_element_by_id(self.digit_button.format(digit))

    def find_add_button_element(self):
        return self.find_element_by_id(self.add_button)

    def find_eq_button_element(self):
        return self.find_element_by_id(self.eq_button)

    def find_result_element(self):
        return self.find_element_by_id(self.result)


class CalculatorHandle(BaseHandle):
    """
    计算器页面-操作层
    """

    def __init__(self):
        self.calculatorPage = CalculatorPage()

    def click_digit_button(self, digit):
        self.calculatorPage.find_digit_button_element(digit).click()

    def click_add_button(self):
        self.calculatorPage.find_add_button_element().click()

    def click_eq_button(self):
        self.calculatorPage.find_eq_button_element().click()

    def get_result_text(self):
        return self.calculatorPage.find_result_element().text

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

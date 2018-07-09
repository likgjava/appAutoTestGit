import os

import pytest

from autotest.datadriven.calculator.page.calculator_page import CalculatorProxy
from autotest.datadriven.calculator.utils import DriverUtil


def data():
    test_data = []
    data_file = os.getcwd() + "/../data/calculator.dat"
    print("data_file=", data_file)
    with open(data_file, encoding='UTF-8') as f:
        for line in f.readlines():
            print(line.strip())
            test_data.append(line.strip().split(','))
    return test_data


class TestCalculator:

    def setup_class(self):
        print('setup_class')
        self.driver = DriverUtil.get_driver()
        self.calculatorProxy = CalculatorProxy()

    def teardown_class(self):
        print('teardown_class')
        DriverUtil.quit_driver()

    def teardown(self):
        print('teardown')
        self.driver.reset()

    @pytest.mark.parametrize("a,b,expect", data())
    def test_add(self, a, b, expect):
        print('a={} b={} expect={}'.format(a, b, expect))

        self.calculatorProxy.add(a, b)

        # 获取计算结果
        result = self.calculatorProxy.get_result()
        assert result == expect


if __name__ == '__main__':
    pytest.main(['test_calculator.py', '-s'])

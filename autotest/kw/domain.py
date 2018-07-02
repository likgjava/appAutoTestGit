class PageElement:
    """
    页面元素
    """

    def __init__(self, element_name, element_desc, location_type, location_value):
        """
        :param element_name: 元素名称
        :param element_desc: 描述
        :param location_type: 定位方式
        :param location_value: 定位值
        """
        self.element_name = element_name
        self.element_desc = element_desc
        self.location_type = location_type
        self.location_value = location_value


class StepData:
    """
    用例步骤测试数据
    """

    def __init__(self, case_code, step_code, input_data, expected_result):
        """
        :param case_code: 用例编号
        :param step_code: 步骤编号
        :param input_data: 输入数据
        :param expected_result: 预期结果
        """
        self.case_code = case_code
        self.step_code = step_code
        self.input_data = input_data
        self.expected_result = expected_result


class CaseStep:
    """
    用例步骤
    """

    def __init__(self, case_code, step_code, step_desc, action, element_name):
        """
        :param case_code: 用例编号
        :param step_code: 步骤编号
        :param step_desc: 步骤描述
        :param action: 执行动作
        :param element_name: 元素名称
        """
        self.case_code = case_code
        self.step_code = step_code
        self.step_desc = step_desc
        self.action = action
        self.element_name = element_name

        # 步骤执行结果
        self.step_execute_result = None
        # 该步骤操作的页面元素
        self.page_element = None
        # 步骤数据
        self.step_data = None


class TestCase:
    """
    用例
    """

    def __init__(self, case_code, case_desc, post_process):
        """
        :param case_code: 用例编号
        :param case_desc: 用例描述
        :param post_process: 后置处理，用例执行完之后需要做的操作
        """
        self.case_code = case_code
        self.case_desc = case_desc
        self.post_process = post_process

        # 执行步骤列表
        self.case_step_list = []

    def get_page(self):
        """
        根据用例编号计算出用例所属页面
        :return: 用例所属页面
        """
        return self.case_code.split('_')[0]


class CaseList:
    """
    用例列表
    """
    # 用例列表
    test_case_list = []


class Report:
    """
    测试报告数据
    """
    # 总用例数
    totalTests = 0
    # 总步骤数
    totalSteps = 0
    # 开始时间
    startTime = 0
    # 结束时间
    endTime = 0
    # 执行总时间(秒)
    takeTime = 0
    # 用例-通过数量
    testPassCount = 0
    # 用例-失败数量
    testFailCount = 0
    # 用例-跳过数量
    testSkipCount = 0
    # 步骤-通过数量
    stepPassCount = 0
    # 步骤-失败数量
    stepFailCount = 0
    # 步骤-跳过数量
    stepSkipCount = 0

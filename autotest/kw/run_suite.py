import time
import traceback

from itcast.autotest.kw.domain import Report
from itcast.autotest.kw.utils import DriverUtil, TestCaseUtil, ReportUtil


def start():
    print('start...')
    driver = DriverUtil.get_driver()

    try:
        report = Report()
        report.startTime = time.time()

        # 加载用例套件
        case_list = TestCaseUtil.load_case_list()

        # 执行用例
        for test_case in case_list.test_case_list:
            print('------start execute case=[{}]'.format(test_case.case_desc))
            TestCaseUtil.execute_test_case(driver, test_case)
            print('------end execute case=[{}]'.format(test_case.case_desc))
        report.endTime = time.time()

        # 生成测试报告
        ReportUtil.create_report(case_list, report)
    except Exception:
        traceback.print_exc()
    finally:
        DriverUtil.quit_driver()


if __name__ == '__main__':
    start()

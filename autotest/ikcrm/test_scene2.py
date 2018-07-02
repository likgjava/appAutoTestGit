import json

import pytest
import time

from itcast.autotest.ikcrm import constant
from itcast.autotest.ikcrm.page.add_cue import AddCueProxy
from itcast.autotest.ikcrm.page.cue import CueProxy
from itcast.autotest.ikcrm.page.home import HomeProxy
from itcast.autotest.ikcrm.page.login import LoginProxy
from itcast.autotest.ikcrm.page.work import WorkProxy
from itcast.autotest.ikcrm.page.work_report import WorkReportProxy
from itcast.autotest.ikcrm.page.write_report import WriteReportProxy
from itcast.autotest.ikcrm.utils import DriverUtil, ToastUtil

test_data = None


def setup_module():
    print('setup_module...')

    # 加载测试数据
    file_path = constant.ROOT_DIR + 'data/test_data.json'
    print('file_path=', file_path)
    global test_data
    test_data = json.load(open(file_path, encoding='UTF-8'))
    print('test_data=', test_data)

    # 加载驱动
    DriverUtil.get_driver()


def teardown_module():
    print('teardown_module...')
    DriverUtil.quit_driver()


class TestLogin:
    loginProxy = LoginProxy()

    @pytest.mark.order(order=1)
    def test_login_username_is_empty(self):
        print('test_login_username_is_empty...')
        data = test_data['login_username_is_empty']
        self.loginProxy.login(data['username'], data['password'])

        element = ToastUtil.get_toast('请输入手机号')
        assert element is not None

    @pytest.mark.order(order=2)
    def test_login_username_is_not_exist(self):
        print('test_login_username_is_not_exist...')
        data = test_data['login_username_is_not_exist']
        self.loginProxy.login(data['username'], data['password'])

        element = ToastUtil.get_toast('帐号不存在')
        assert element is not None

    @pytest.mark.order(order=3)
    def test_login_password_is_empty(self):
        print('test_login_password_is_empty...')
        data = test_data['login_password_is_empty']
        print('login_password_is_empty data=', data)
        self.loginProxy.login(data['username'], data['password'])

        element = ToastUtil.get_toast('请输入密码')
        assert element is not None

    @pytest.mark.order(order=4)
    def test_login_password_is_error(self):
        print('test_login_password_is_error...')
        data = test_data['login_password_is_error']
        print('login_password_is_error data=', data)
        self.loginProxy.login(data['username'], data['password'])

        element = ToastUtil.get_toast('密码错误')
        assert element is not None

    @pytest.mark.order(order=5)
    def test_login(self):
        print('test_login...')
        login = test_data['csdn']
        print('csdn data=', login)
        self.loginProxy.login(login['username'], login['password'])

    def teardown(self):
        print('teardown...')
        # DriverUtil.get_driver().reset()
        time.sleep(1)


# @pytest.mark.skip
class TestWriteReport:
    homeProxy = HomeProxy()
    workProxy = WorkProxy()
    workReportProxy = WorkReportProxy()
    writeReportProxy = WriteReportProxy()

    @pytest.mark.order(order=1)
    def test_write_report_summary_is_empty(self):
        print('test_write_report_summary_is_empty...')

        # 进入工作页面
        self.homeProxy.entry_work_page()

        # 进入工作报告页面
        self.workProxy.entry_work_report_page()

        # 进入写日报页面
        self.workReportProxy.entry_add_report_page()

        # 写报告
        data = test_data['write_report_summary_is_empty']
        self.writeReportProxy.write_report(data['summary'], data['plan'], data['read_over'])

        # 验证是否提交成功
        element = ToastUtil.get_toast('总结不能为空')
        assert element is not None

    @pytest.mark.order(order=2)
    def test_write_report_plan_is_empty(self):
        print('test_write_report_plan_is_empty...')

        # 进入工作页面
        self.homeProxy.entry_work_page()

        # 进入工作报告页面
        self.workProxy.entry_work_report_page()

        # 进入写日报页面
        self.workReportProxy.entry_add_report_page()

        # 写报告
        data = test_data['write_report_plan_is_empty']
        self.writeReportProxy.write_report(data['summary'], data['plan'], data['read_over'])

        # 验证
        element = ToastUtil.get_toast('计划不能为空')
        assert element is not None

    @pytest.mark.order(order=3)
    def test_write_report_read_over_is_empty(self):
        print('test_write_report_read_over_is_empty...')

        # 进入工作页面
        self.homeProxy.entry_work_page()

        # 进入工作报告页面
        self.workProxy.entry_work_report_page()

        # 进入写日报页面
        self.workReportProxy.entry_add_report_page()

        # 写报告
        data = test_data['write_report_read_over_is_empty']
        self.writeReportProxy.write_report(data['summary'], data['plan'], data['read_over'])

        # 验证
        element = ToastUtil.get_toast('批阅人不能为空')
        assert element is not None

    @pytest.mark.order(order=4)
    def test_write_report(self):
        print('test_write_report...')

        # 进入工作页面
        self.homeProxy.entry_work_page()

        # 进入工作报告页面
        self.workProxy.entry_work_report_page()

        # 进入写日报页面
        self.workReportProxy.entry_add_report_page()

        # 写报告
        write_report = test_data['write_report']
        print('write_report data=', write_report)
        self.writeReportProxy.write_report(write_report['summary'], write_report['plan'], write_report['read_over'])

        # 验证
        element = ToastUtil.get_toast('提交成功')
        assert element is not None

    def teardown(self):
        print('switch_to_home_page...')
        self.homeProxy.switch_to_home_page()
        time.sleep(3)


# @pytest.mark.skip
class TestAddCue:
    homeProxy = HomeProxy()
    workProxy = WorkProxy()
    cueProxy = CueProxy()
    addCueProxy = AddCueProxy()

    @pytest.mark.order(order=1)
    def test_add_cue(self):
        print('test_add_cue...')
        # 进入工作页面
        self.homeProxy.entry_work_page()

        # 进入线索页面
        self.workProxy.entry_work_report_page()

        # 进入新增线索页面
        self.cueProxy.entry_add_cue_page()

        # 新增线索
        data = test_data['add_cue']
        print('add_cue data=', data)
        self.addCueProxy.add_cue(data['name'], data['company_name'], data['phone'])

        # 验证
        element = ToastUtil.get_toast('保存成功')
        assert element is not None

    def teardown(self):
        print('switch_to_home_page...')
        self.homeProxy.switch_to_home_page()


if __name__ == '__main__':
    pytest.main(['test_scene2.py', '-s', '--alluredir=allure-result'])

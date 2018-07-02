import time

import allure
import pytest

from itcast.autotest.ikcrm import constant
from itcast.autotest.ikcrm.utils import DriverUtil


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # print('rep=====', rep)

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        print('出现异常了=', rep)

        screenshot = constant.ROOT_DIR + 'screenshot/' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.png'
        DriverUtil.get_driver().save_screenshot(screenshot)
        f = open(screenshot, 'rb').read()
        allure.attach('失败截图', f, allure.attach_type.PNG)

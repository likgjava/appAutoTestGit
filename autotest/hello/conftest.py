import pytest
import os.path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # print('rep=====', rep)

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        print('出现异常了。。。', rep.nodeid)


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print("setting up======111111111111111111111111111111111111111111111111111111111======", item)



def pytest_runtest_teardown(item, nextitem):
    print("pytest_runtest_teardown======1111111111======", item)
    print("pytest_runtest_teardown======2222222222======", nextitem)
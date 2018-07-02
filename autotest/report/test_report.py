import pytest


def test_a():
    print('aaa')


def test_b():
    print('bbb')
    assert 0


if __name__ == '__main__':
    # pytest.main(['test_report.py', '--resultlog=./log.txt'])
    # pytest.main(['test_report.py', '--junitxml=./log.xml'])
    pytest.main(['test_report.py', '--html=report/report.html'])

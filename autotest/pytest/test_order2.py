import pytest

@pytest.mark.run(order=1)
class Test02:
    def test_a(s):
        print('aaa222')

    @pytest.mark.run(after='test_c')
    def test_b(s):
        print('bbb2222')

    def test_c(s):
        print('ccc2222')


if __name__ == '__main__':
    pytest.main(['test_order.py'])

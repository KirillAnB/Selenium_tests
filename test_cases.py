import pytest

cases = [('Kirill', 'Julia'),('Alexandr', 'Julia'),('Kirill', 'Kirill')]
@pytest.mark.xfail
@pytest.mark.allure
@pytest.mark.parametrize("man, woman", cases)
def test_nums(man, woman):
    assert man != woman, 'OOOPS'

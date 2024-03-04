import pytest

@pytest.mark.order(5)
def test_first():
    print("first")
    assert True

@pytest.mark.order(2)
def test_second():
    print("second")
    assert True

@pytest.mark.order(3)
def test_third():
    print("third")
    assert True

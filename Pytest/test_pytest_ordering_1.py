import pytest

@pytest.mark.run(order=4)
def test_first():
    print("1")
    assert True

@pytest.mark.run(order=2)
def test_second():
    print("2")
    assert True

@pytest.mark.run(order=3)
def test_third():
    print("3")
    assert True

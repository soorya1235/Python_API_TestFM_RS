import pytest

@pytest.fixture(autouse=True,scope="class")
def autouse_fixture():
    print("Autouse fixture setup")

def test_function():
    print("Test function")

class TestClass:
    def test_method_1(self):
        print("Test method")

    def test_method_2(self):
        print("Test method")

    def test_method_3(self):
        print("Test method")

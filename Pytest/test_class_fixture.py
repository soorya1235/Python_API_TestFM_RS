import pytest


@pytest.mark.usefixtures("test_fixture_two")
class Test_class:

    def test_class_one(self):
        print("test_class_one")

    def test_class_two(self):
        print("test_class_one")

    def test_class_three(self):
        print("test_class_one")

import pytest

# Fixture with session scope
@pytest.fixture(scope="session")
def session_fixture():
    print("\nSetup for session_fixture")
    yield
    print("Teardown for session_fixture")

# Fixture with module scope
@pytest.fixture(scope="module")
def module_fixture():
    print("\nSetup for module_fixture")
    yield
    print("Teardown for module_fixture")

# Fixture with class scope
@pytest.fixture(scope="class")
def class_fixture():
    print("\nSetup for class_fixture")
    yield
    print("Teardown for class_fixture")

# Fixture with function scope
@pytest.fixture(scope="function")
def function_fixture():
    print("Setup for function_fixture")
    yield
    print("Teardown for function_fixture")

# Test classcls
@pytest.mark.usefixtures("session_fixture", "module_fixture")
class TestScopeOrder:
    @pytest.mark.usefixtures("class_fixture")
    def test_method(self, function_fixture):
        print("Test method")

    @pytest.mark.usefixtures("class_fixture")
    def test_another_method(self, function_fixture):
        print("Another test method")

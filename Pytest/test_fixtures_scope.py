import pytest

# Fixture with function scope
@pytest.fixture(scope="function")
def function_fixture():
    print("Setup for function_fixture")
    yield
    print("Teardown for function_fixture")

# Fixture with class scope
@pytest.fixture(scope="class")
def class_fixture():
    print("Setup for class_fixture")
    yield
    print("Teardown for class_fixture")

# Fixture with module scope
@pytest.fixture(scope="module")
def module_fixture():
    print("Setup for module_fixture")
    yield
    print("Teardown for module_fixture")

# Fixture with session scope
@pytest.fixture(scope="session")
def session_fixture():
    print("Setup for session_fixture")
    yield
    print("Teardown for session_fixture")

# Test function using fixtures
def test_with_fixtures(function_fixture, class_fixture, module_fixture, session_fixture):
    print("Test function")

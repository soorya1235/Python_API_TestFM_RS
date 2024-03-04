import pytest

@pytest.fixture
def test_fixture_one():
    print("Calling before fixture")
    yield
    print("Called after fixutre")


@pytest.fixture(scope="class")
def test_fixture_two():
    print("Called before Class")
    yield
    print("Called after class")


@pytest.fixture(autouse=True)
def test_auto_fixture():
    print("This is autouse fixture")

@pytest.fixture(params=[1,2,3])
def test_return_param(request):
    return request.param

@pytest.fixture
def return_dataload():
    return [1,2,3,4,5]





import pytest

def function_that_raises():
    raise ZeroDivisionError("hello this world")

def test_function_that_raises():
    with pytest.raises(ValueError):
        function_that_raises()

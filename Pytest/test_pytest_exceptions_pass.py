import pytest

def function_that_raises():
    raise ValueError("This is an example error")

def test_function_that_raises():
    with pytest.raises(ValueError):
        function_that_raises()

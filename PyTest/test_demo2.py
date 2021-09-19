import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_third():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string not match."

def test_fourthCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "sum does not match"
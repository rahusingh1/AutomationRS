import pytest


@pytest.mark.smoke
def test_first(setup):
    print("Hello! Rahul")

@pytest.mark.xfail
def test_secondCreditCard():
    print("India")

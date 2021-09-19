import pytest


@pytest.fixture(scope='class')
def setup():
    print("i will be executing first")
    yield
    print("\ni will be executing last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["rahul","singh","rahulsinghacademy.com"]


@pytest.fixture(params=[("chrome","rahul","singh"), ("firefox","singh"),"IE"])
def crossBrowser(request):
    return request.param
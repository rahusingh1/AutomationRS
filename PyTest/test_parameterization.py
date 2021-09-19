import pytest

@pytest.mark.usefixtures
def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[0])
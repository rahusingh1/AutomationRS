import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtures(self):
        print('i will be executing steps in fixtures method')

    def test_fixtures1(self):
        print('i will be executing steps in fixtures1 method')

    def test_fixtures2(self):
        print('i will be executing steps in fixtures2 method')

    def test_fixtures3(self):
        print('i will be executing steps in fixtures3 method')

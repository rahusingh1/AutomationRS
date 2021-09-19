import pytest

from PyTest.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_userprofile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        log = self.getLogger()
        log.info(dataLoad[0])
        print(dataLoad[2])
        log.info(dataLoad[2])
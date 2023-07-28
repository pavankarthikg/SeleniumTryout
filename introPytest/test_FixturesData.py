import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample:
    def test_editProfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[0])

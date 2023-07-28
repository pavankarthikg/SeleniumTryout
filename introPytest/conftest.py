import pytest


@pytest.fixture()
def bark():
    print("Early bark")
    yield
    print("Last")
@pytest.fixture()
def dataLoad():
    print("Profile")
    return ["Pavan", "Karthik"]

@pytest.fixture(params=["chrome","Firefox", "IE"])
def crossBrowser(request):
    return request.param
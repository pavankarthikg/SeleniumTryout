import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_introPyt():
    msg="Hello"
    assert msg == "Hi", "Test failed"

def test_code1():
    a, b, c = 4, 6, 8
    assert a+2 == b == c-2, "Math is not mathing"

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
import pytest

@pytest.mark.parametrize("username, password", [("sudip","sudip"),("sudip","khati")])
def test_method(username, password):
    assert username == password
import pytest
@pytest.fixture
def tester():
    name = "Sudip"
    contact = 9861758420
    return [name, contact]

def testing_1(tester):
    first_name = "Sudip"
    assert tester[0] == first_name

def testing_2(tester):

    contact_num = 9861758420
    assert tester[1] == contact_num
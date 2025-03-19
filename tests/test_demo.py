import pytest


@pytest.fixture()
def setup():
    print("I run 1st")
    yield
    print("I run last")

def test_firstProgram(setup):
    msg = 'Hello'
    assert msg == 'Hello', 'Test Failed'

def test_secondProgram(setup):
    print('Hi')
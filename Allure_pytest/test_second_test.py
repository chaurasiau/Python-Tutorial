import pytest


def test_success2():
    """this test succeeds"""
    assert True


def test_failure2():
    """this test fails"""
    assert False


def test_skip2():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken2():
    raise Exception('oops')

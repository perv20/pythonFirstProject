import pytest


def test_addition():
    assert 1 - 1 == 2


@pytest.mark.smoke
def test_sub():
    assert 1 - 1 == 0

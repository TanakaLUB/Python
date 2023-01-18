import pytest

# fixtureであることを示すデコレータ


@pytest.fixture()
def my_fixture_1():
    return "hello"

# fixtureを引数として渡す


def test_foo(my_fixture_1):
    assert my_fixture_1 == "hello"

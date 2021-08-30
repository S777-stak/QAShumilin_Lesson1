import pytest

from Lesson_16.function_test.code_for_testing import Human


def test_check_alive_after_100(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__age", 101
    )
    human.grow()
    assert human.__status == "dead"

@pytest.mark.xfail(reason="Failes due to existing bug", condition=True)
def test_check_gender_after_change_from_female(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__gender", "female"
    )
    human.change_gender("male")

    assert human.gender == "female"

def test_check_raise_of_exception_for_chenge_gender(human):
    with pytest.raises(Exception):
        human.change_gender("")
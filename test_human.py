import pytest

from Lesson_16.function_test.code_for_testing import Human


def test_check_alive_after_100(human, monkeypatch):
    monkeypatch.setattr(
        human, "dead", 101
    )
    human.grow()
    assert human.grow == 100




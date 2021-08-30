import pytest

from Lesson_16.function_test.code_for_testing import Human

@pytest.fixture(scope="module")

def human() -> Human:
    print("Setup for test")
    yield Human("John", 101, "male")




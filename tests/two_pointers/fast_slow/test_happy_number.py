import pytest
from solutions.two_pointers.fast_slow.happy_number import Solution

@pytest.mark.parametrize("number, expected", [
        (19, True),
        (2, False),
        (1, True),
        (7, True),
        (20, False)
    ])
def test_is_happy(number, expected):
    solution = Solution()
    assert solution.isHappy(number) == expected

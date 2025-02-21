import pytest
from solutions.binary_search.speed_to_eat_bananas import Solution

@pytest.mark.parametrize("piles, h, expected", [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),
    ([312884470], 312884469, 2),
    ([1, 1, 1, 1], 4, 1)
])
def test_minEatingSpeed(piles, h, expected):
    sol = Solution()
    assert sol.minEatingSpeed(piles, h) == expected
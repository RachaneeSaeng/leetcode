import pytest
from solutions.two_pointers.sliding_window.longest_ones import Solution

@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
    ([0,0,1,1,1,0,0], 0, 3),
    ([0,0,1,1,1,0,0,1,1,1,1,0], 2, 9),
    ([1,1,1,1,1], 0, 5),
    ([0,0,0,0], 2, 2),
    ([1,0,1,0,1,0,1,0,1,0], 5, 10)
])
def test_longest_ones(nums, k, expected):
    solution = Solution()
    assert solution.longestOnes(nums, k) == expected
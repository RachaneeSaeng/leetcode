import pytest
from solutions.misc.two_sum import Solution

@pytest.mark.parametrize("numbers, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 2, 3, 4, 5], 9, [3, 4]),
    ([0, 4, 3, 0], 0, [0, 3]),
    ([-3, 4, 3, 90], 0, [0, 2]),
    ([1, 5, 1, 5], 10, [1, 3])
])
def test_two_sum(numbers, target, expected):
    solution = Solution()
    assert solution.twoSum(numbers, target) == expected
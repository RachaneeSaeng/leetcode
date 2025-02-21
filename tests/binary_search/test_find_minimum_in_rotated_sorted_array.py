import pytest
from solutions.binary_search.find_minimum_in_rotated_sorted_array import Solution

@pytest.mark.parametrize("nums, expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([2, 1], 1),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([5, 6, 7, 8, 9, 1, 2, 3, 4], 1),
    ([2, 3, 4, 5, 6, 7, 8, 9, 1], 1),
])
def test_find_min(nums, expected):
    assert Solution().findMin(nums) == expected
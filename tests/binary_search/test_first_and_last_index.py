import pytest
from solutions.binary_search.first_and_last_index import Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([1], 1, [0, 0]),
    ([2, 2], 2, [0, 1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [4, 4]),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, [0, 9]),
])
def test_searchRange(nums, target, expected):
    solution = Solution()
    assert solution.searchRange(nums, target) == expected
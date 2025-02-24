import pytest
from solutions.two_pointers.sliding_window.largest_subarray_sum import Solution

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5], 2, 9),  # Subarray [4, 5]
    ([1, -2, 3, 4, -5, 6], 4, 8),  # Subarray [3, 4, -5, 6]
    ([1, 2, 3, 4, 5], 1, 5),  # Subarray [5]
    ([1, 2, 3, 4, 5], 5, 15),  # Subarray [1, 2, 3, 4, 5]
    ([1, 2, 3, 4, 5], 3, 12),  # Subarray [3, 4, 5]
    ([1, 2, 3, 7, 4, 1], 3, 14),  # Subarray [3, 7, 4]
])
def test_largestSubarray(nums, k, expected):
    solution = Solution()
    assert solution.largestSubarray(nums, k) == expected
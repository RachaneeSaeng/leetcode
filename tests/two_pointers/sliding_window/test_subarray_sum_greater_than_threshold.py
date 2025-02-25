import pytest
from solutions.two_pointers.sliding_window.subarray_sum_greater_than_threshold import Solution

@pytest.mark.parametrize("arr, k, threshold, expected", [    
    ([11,13,17,23,29,31,7,5,2,3], 3, 5, 6),
    ([2,2,2,2,5,5,5,8], 3, 4, 3),
])
def test_numOfSubarrays(arr, k, threshold, expected):
    sol = Solution()
    assert sol.numOfSubarrays(arr, k, threshold) == expected
import pytest
from solutions.binary_search.the_peak_of_a_mountain_array import Solution

@pytest.mark.parametrize("arr, expected", [
    ([0, 2, 1, 0], 1),
    ([0, 10, 5, 2], 1),
    ([3, 4, 5, 1], 2),
    ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
    ([1, 3, 5, 4, 2], 2),
])
def test_peakIndexInMountainArray(arr, expected):
    sol = Solution()
    assert sol.peakIndexInMountainArray(arr) == expected
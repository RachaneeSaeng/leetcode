import pytest
from solutions.heap.k_closest_elements import Solution

@pytest.mark.parametrize("arr, k, x, expected", [
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, 6, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 2, 3, [2, 3]),
    ([1, 2, 3, 4, 5], 3, 3, [2, 3, 4]),
    ([1, 2, 3, 4, 5], 1, 3, [3]),
    ([1, 2, 3, 4, 5], 5, 3, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 3, 2, [1, 2, 3]),
    ([1, 2, 3, 4, 5], 3, 4, [3, 4, 5]),
    ([1,1,2,3,4,5], 4, -1, [1, 1, 2, 3]),
    ([1,1,2,3,4,5], 5, 10, [1, 2, 3, 4, 5]),
    ([1,1,1,10,10,10], 1, 9, [10]),
])
def test_findClosestElements(arr, k, x, expected):
    sol = Solution()
    assert sol.findClosestElements(arr, k, x) == expected
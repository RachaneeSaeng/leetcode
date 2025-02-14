import pytest
from solutions.heap.kth_smallest_in_sorted_matrix import Solution

@pytest.mark.parametrize("matrix, k, expected", [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
    ([[1, 2], [1, 3]], 2, 1),
    ([[1, 2], [3, 4]], 3, 3),
    ([[1]], 1, 1),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, 5)
])
def test_kthSmallest(matrix, k, expected):
    sol = Solution()
    assert sol.kthSmallest(matrix, k) == expected
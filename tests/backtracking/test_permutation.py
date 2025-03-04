import pytest
from solutions.backtracking.permutation import Solution

def test_permute_empty():
    sol = Solution()
    assert sol.permute([]) == [[]]

def test_permute_single_element():
    sol = Solution()
    assert sol.permute([1]) == [[1]]

def test_permute_two_elements():
    sol = Solution()
    result = sol.permute([1, 2])
    expected = [[1, 2], [2, 1]]
    assert sorted(result) == sorted(expected)

def test_permute_three_elements():
    sol = Solution()
    result = sol.permute([1, 2, 3])
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    assert sorted(result) == sorted(expected)

if __name__ == "__main__":
    pytest.main()
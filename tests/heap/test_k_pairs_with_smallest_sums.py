import pytest
from solutions.heap.k_pairs_with_smallest_sums import Solution

@pytest.fixture
def solution():
    return Solution()

def test_k_smallest_pairs_case1(solution):   
    assert solution.kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]

def test_k_smallest_pairs_case2(solution):   
    assert solution.kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]

def test_k_smallest_pairs_case2_1(solution):   
    assert solution.kSmallestPairs([1,1,2], [1,2,3], 3) == [[1,1],[1,1],[1,2]]

def test_k_smallest_pairs_case3(solution):   
    assert solution.kSmallestPairs([1,2], [3], 3) == [[1,3],[2,3]]

def test_k_smallest_pairs_case4(solution):   
    assert solution.kSmallestPairs([1,2,3], [1,2,3], 3) == [[1,1],[1,2],[2,1]]

def test_k_smallest_pairs_case5(solution):   
    assert solution.kSmallestPairs([], [1,2,3], 3) == []

def test_k_smallest_pairs_case7(solution):   
    assert solution.kSmallestPairs([1,2,3], [1,2,3], 0) == []

if __name__ == "__main__":
    pytest.main()
import pytest
from solutions.heap.kth_largest_element import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findKthLargest_case1(solution):
    assert solution.findKthLargest([3,2,1,5,6,4], 2) == 5

def test_findKthLargest_case2(solution):
    assert solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_findKthLargest_case3(solution):
    assert solution.findKthLargest([1], 1) == 1

def test_findKthLargest_case4(solution):
    assert solution.findKthLargest([7,6,5,4,3,2,1], 3) == 5

def test_findKthLargest_case5(solution):
    assert solution.findKthLargest([2,1], 2) == 1
    
def test_findKthLargest_case6(solution):
    assert solution.findKthLargest([3,2], 2) == 2

if __name__ == "__main__":
    pytest.main()
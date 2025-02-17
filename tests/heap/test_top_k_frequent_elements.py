import pytest
from solutions.heap.top_k_frequent_elements import Solution

@pytest.fixture
def solution():
    return Solution()

def test_kth_most_frequent_elements_multi_element(solution):
    assert solution.topKFrequent([1,1,1,2,2,3], 2) == [2,1]
    
def test_kth_most_frequent_elements_single_element(solution):
    assert solution.topKFrequent([1], 1) == [1]
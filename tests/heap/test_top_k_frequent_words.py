import pytest
from solutions.heap.top_k_frequent_words import Solution

@pytest.fixture
def solution():
    return Solution()

def test_kth_most_frequent_words_1(solution):
    assert solution.topKFrequent(["i","love","leetcode","i","love","coding"], 2) == ["i", "love"]
    
def test_kth_most_frequent_words_3(solution):
    assert solution.topKFrequent(["i","love","leetcode","i","love","coding"], 3) == ["i", "love", "coding"]
    
def test_kth_most_frequent_words_2(solution):
    assert solution.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) == ["the","is","sunny","day"]
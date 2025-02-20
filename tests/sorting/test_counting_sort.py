import pytest
from solutions.sorting.counting_sort import counting_sort

def test_counting_sort_empty():
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    assert counting_sort([1]) == [1]

def test_counting_sort_sorted():
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_counting_sort_reverse_sorted():
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_counting_sort_unsorted():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_with_duplicates():
    assert counting_sort([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]

def test_counting_sort_with_negative_numbers():
    assert counting_sort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1]

def test_counting_sort_mixed_numbers():
    assert counting_sort([3, -2, -1, 0, 2, 1, -3]) == [-3, -2, -1, 0, 1, 2, 3]

if __name__ == "__main__":
    pytest.main()
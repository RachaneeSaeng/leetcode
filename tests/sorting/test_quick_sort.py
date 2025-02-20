import pytest
from solutions.sorting.quick_sort import quick_sort

def test_quick_sort_empty():
    array = []
    quick_sort(array, 0, len(array) - 1)
    assert array == []

def test_quick_sort_single_element():
    array = [1]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1]

def test_quick_sort_sorted():
    array = [1, 2, 3, 4, 5]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    array = [5, 4, 3, 2, 1]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2, 3, 4, 5]

def test_quick_sort_unsorted():
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 5, 7, 8, 9, 10]

def test_quick_sort_duplicates():
    array = [4, 2, 2, 8, 3, 3, 1]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2, 2, 3, 3, 4, 8]
    
def test_quick_sort_from_structify():
    array = [14, 2, 16, 21, 35, 31, 46, 18]
    quick_sort(array, 0, len(array) - 1)
    assert array == [2, 14, 16, 18, 21, 31, 35, 46]

if __name__ == "__main__":
    pytest.main()
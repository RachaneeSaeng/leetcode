import pytest
from solutions.sorting.merge_sort import merge_sort

def test_merge_sort_empty():
    array = []
    merge_sort(array)
    assert array == []

def test_merge_sort_single_element():
    array = [1]
    merge_sort(array)
    assert array == [1]

def test_merge_sort_sorted():
    array = [1, 2, 3, 4, 5]
    merge_sort(array)
    assert array == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    array = [5, 3, 1, 4, 2]
    merge_sort(array)
    assert array == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    array = [4, 2, 2, 3, 1, 4]
    merge_sort(array)
    assert array == [1, 2, 2, 3, 4, 4]

def test_merge_sort_negative_numbers():
    array = [3, -1, 2, -5, 0]
    merge_sort(array)
    assert array == [-5, -1, 0, 2, 3]

def test_merge_sort_mixed_numbers():
    array = [3, -1, 2, 0, -5, 4]
    merge_sort(array)
    assert array == [-5, -1, 0, 2, 3, 4]

def test_merge_sort_large_numbers():
    array = [1000, 500, 100, 50, 10]
    merge_sort(array)
    assert array == [10, 50, 100, 500, 1000]
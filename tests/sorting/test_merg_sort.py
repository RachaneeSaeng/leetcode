import pytest
from solutions.sorting.merge_sort import merge_sort

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]

def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    assert merge_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    assert merge_sort([4, 2, 2, 3, 1, 4]) == [1, 2, 2, 3, 4, 4]

def test_merge_sort_negative_numbers():
    assert merge_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3]

def test_merge_sort_mixed_numbers():
    assert merge_sort([3, -1, 2, 0, -5, 4]) == [-5, -1, 0, 2, 3, 4]

def test_merge_sort_large_numbers():
    assert merge_sort([1000, 500, 100, 50, 10]) == [10, 50, 100, 500, 1000]
import pytest
from solutions.sorting.heap_sort import heap_sort

def test_heap_sort_empty():
    arr = []
    heap_sort(arr)
    assert arr == []

def test_heap_sort_single_element():
    arr = [1]
    heap_sort(arr)
    assert arr == [1]

def test_heap_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    heap_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    heap_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_heap_sort_unsorted():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heap_sort(arr)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_heap_sort_duplicates():
    arr = [2, 3, 2, 3, 2, 3]
    heap_sort(arr)
    assert arr == [2, 2, 2, 3, 3, 3]

def test_heap_sort_negative_numbers():
    arr = [-1, -3, -2, -4, -5]
    heap_sort(arr)
    assert arr == [-5, -4, -3, -2, -1]

def test_heap_sort_mixed_numbers():
    arr = [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
    heap_sort(arr)
    assert arr == [-6, -5, -5, -1, 1, 2, 3, 3, 4, 5, 9]
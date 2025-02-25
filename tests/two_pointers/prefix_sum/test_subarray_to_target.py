import pytest
from solutions.two_pointers.prefix_sum.subarray_sum_to_target import Solution

def test_subarray_sum_empty():
    assert Solution().subarraySum([], 0) == 0

def test_subarray_sum_single_element_1():
    assert Solution().subarraySum([1], 1) == 1

def test_subarray_sum_single_element_2():
    assert Solution().subarraySum([1], 2) == 0

def test_subarray_sum_multiple_elements_1():
    assert Solution().subarraySum([1, 1, 1], 2) == 2

def test_subarray_sum_multiple_elements_2():
    assert Solution().subarraySum([1, 2, 3], 3) == 2

def test_subarray_sum_multiple_elements_3():
    assert Solution().subarraySum([1, 2, 3], 6) == 1

def test_subarray_sum_multiple_elements_4():
    assert Solution().subarraySum([1, 2, 3], 7) == 0    

def test_subarray_sum_negative_numbers_1():
    assert Solution().subarraySum([-1, -1, 1], 0) == 1

def test_subarray_sum_negative_numbers_2():
    assert Solution().subarraySum([-1, -1, 1], -2) == 1

def test_subarray_sum_negative_numbers_3():
    assert Solution().subarraySum([-1, -1, 1], -1) == 3

def test_subarray_sum_mixed_numbers_1():
    assert Solution().subarraySum([1, -1, 2, 3], 3) == 1

def test_subarray_sum_mixed_numbers_2():
    assert Solution().subarraySum([1, -1, 2, 3], 4) == 1

def test_subarray_sum_mixed_numbers_3():
    assert Solution().subarraySum([1, -1, 2, 3], 0) == 1
    
def test_subarray_sum_mixed_numbers_4():
    assert Solution().subarraySum([1,-1,0], 0) == 3

if __name__ == "__main__":
    pytest.main()
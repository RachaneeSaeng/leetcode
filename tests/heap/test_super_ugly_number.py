import pytest
from solutions.heap.super_ugly_number import Solution

@pytest.fixture
def solution():
    return Solution()
    
def test_nthSuperUglyNumber_case1(solution):
    assert solution.nthSuperUglyNumber(19, [2, 3, 19]) == 57

def test_nthSuperUglyNumber_case2(solution):
    assert solution.nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32

def test_nthSuperUglyNumber_case3(solution):
    assert solution.nthSuperUglyNumber(1, [2, 3, 5]) == 1

def test_nthSuperUglyNumber_case4(solution):
    assert solution.nthSuperUglyNumber(6, [2, 3, 5]) == 6

def test_nthSuperUglyNumber_case5(solution):
    assert solution.nthSuperUglyNumber(8, [2, 3, 5]) == 9

def test_nthSuperUglyNumber_case6(solution):
    assert solution.nthSuperUglyNumber(15, [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 29

def test_nthSuperUglyNumber_case7(solution):
    assert solution.nthSuperUglyNumber(10, [2, 3, 5]) == 12

def test_nthSuperUglyNumber_case8(solution):
    assert solution.nthSuperUglyNumber(5, [2, 3, 5]) == 5

if __name__ == "__main__":
    pytest.main()
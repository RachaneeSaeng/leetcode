import pytest
from solutions.two_pointers.sliding_window.min_consecutive_cards import Solution

def test_minimumCardPickup_case6():
    solution = Solution()
    assert solution.minimumCardPickup([3,4,2,3,4,7]) == 4

def test_minimumCardPickup_case7():
    solution = Solution()
    assert solution.minimumCardPickup([1,0,5,3]) == -1
    
def test_minimumCardPickup_case8():
    solution = Solution()
    assert solution.minimumCardPickup([70,37,70,41,1,62,71,49,38,50,29,76,29,41,22,66,88,18,85,53]) == 3

if __name__ == "__main__":
    pytest.main()
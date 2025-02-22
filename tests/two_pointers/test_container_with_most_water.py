import pytest
from solutions.two_pointers.container_with_most_water import Solution

def test_max_area():
    solution = Solution()
    
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea([1,1]) == 1
    assert solution.maxArea([4,3,2,1,4]) == 16
    assert solution.maxArea([1,2,1]) == 2
    assert solution.maxArea([1,2,4,3]) == 4

if __name__ == "__main__":
    pytest.main()
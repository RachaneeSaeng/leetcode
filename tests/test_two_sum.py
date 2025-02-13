import pytest
from solutions.two_sum import Solution

def test_two_sum():
    assert Solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution.two_sum([3, 2, 4], 6) == [1, 2]
    assert Solution.two_sum([3, 3], 6) == [0, 1]
    assert Solution.two_sum([1, 2, 3, 4, 5], 10) == []
    assert Solution.two_sum([0, 4, 3, 0], 0) == [0, 3]
    assert Solution.two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

if __name__ == "__main__":
    pytest.main()
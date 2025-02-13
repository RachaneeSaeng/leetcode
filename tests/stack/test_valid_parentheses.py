import pytest
from solutions.stack.valid_parentheses import Solution

@pytest.fixture
def solution():
    return Solution()

def test_valid_parentheses(solution):
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("{[]}") == True
    assert solution.isValid("") == True
    assert solution.isValid("(((((((())))))))") == True
    assert solution.isValid("(((((((()))))))") == False
    assert solution.isValid("{[()]}") == True
    assert solution.isValid("{[(])}") == False
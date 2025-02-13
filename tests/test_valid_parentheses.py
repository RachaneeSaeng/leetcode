import pytest
from solutions.valid_parentheses import Solution

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("{", False),
    ("}", False),
    ("[", False),
    ("]", False),
    ("{[()()]}", True),
    ("{[()()]}{", False),
    ("{[()()]}}", False),
])
def test_isValid(s, expected):
    solution = Solution()
    assert solution.isValid(s) == expected
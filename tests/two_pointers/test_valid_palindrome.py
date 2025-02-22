import pytest
from solutions.two_pointers.valid_palindrome import Solution

@pytest.mark.parametrize("input_str, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    (" ", True),
    ("a.", True),
    ("0P", False),
    ("ab_a", True),
    ("Do geese see God?", True),
    ("Was it a car or a cat I saw?", True),
    ("A brown fox jumping over", False),
])
def test_is_palindrome(input_str, expected):
    solution = Solution()
    assert solution.isPalindrome(input_str) == expected
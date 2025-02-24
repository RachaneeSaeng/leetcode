import pytest
from solutions.two_pointers.sliding_window.longest_substring_without_repeating_chars import Solution

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("abcdef", 6),
    ("aab", 2),
    ("dvdf", 3),
    ("anviaj", 5),
    ("tmmzuxt", 5)
])
def test_lengthOfLongestSubstring(s, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected
import pytest
from solutions.two_pointers.sliding_window.find_all_anagrams import Solution

@pytest.mark.parametrize("s, p, expected", [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("af", "be", []),
    ("baa", "aa", [1]),
    ("acdcaeccde", "c", [1, 3, 6, 7]),
    ("aaaaaaaaaa", "aaaaaaaaaaaaa", []),
    ("abcabcabc", "abc", [0, 1, 2, 3, 4, 5, 6]),
])
def test_find_all_anagrams(s, p, expected):
    assert Solution().findAnagrams(s, p) == expected
import pytest
from solutions.two_pointers.sliding_window.vowel_substring import Solution

@pytest.fixture
def solution():
    return Solution()

def test_countVowelSubstrings_empty_string(solution):
    assert solution.countVowelSubstrings("") == 0

def test_countVowelSubstrings_no_vowels(solution):
    assert solution.countVowelSubstrings("unicornarihan") == 0

def test_countVowelSubstrings_all_vowels(solution):
    assert solution.countVowelSubstrings("aeiou") == 1

def test_countVowelSubstrings_all_vowels_2(solution):
    assert solution.countVowelSubstrings("aeiouu") == 2

def test_countVowelSubstrings_mixed_characters(solution):
    assert solution.countVowelSubstrings("aeiobcdfg") == 0

def test_countVowelSubstrings_multiple_vowel_substrings(solution):
    assert solution.countVowelSubstrings("aeiouaeiou") == 21

def test_countVowelSubstrings_vowels_within_consonants(solution):
    assert solution.countVowelSubstrings("abcdeiouxyz") == 0

def test_countVowelSubstrings_vowels_at_edges(solution):
    assert solution.countVowelSubstrings("aeioubcdfg") == 1

def test_countVowelSubstrings_vowels_multiple(solution):
    assert solution.countVowelSubstrings("cuaieuouac") == 7
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        latest_consonant = -1
        vowel_latest_positions = {}
        result = 0
        for i in range(len(word)):
            c = word[i]
            if c in 'aeiou':
                vowel_latest_positions[c] = i
                if len(vowel_latest_positions.keys()) == 5:
                    # possible vowel substring variants are to include or exclude the optional vowels between the latest consonant and the first vowel
                    # (chars after the first vowel is needed to ensure 5 vowels are present)
                    result += min(vowel_latest_positions.values()) - latest_consonant 
            else:
                latest_consonant = i
                vowel_latest_positions = {}
        return result
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# https://algo.monster/problems/longest_substring_without_repeating_characters

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_positions = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            if char in char_positions:
                start = max(start, char_positions[char] + 1) # use max to ignore char that already be omitted
                
            char_positions[char] = end
            max_length = max(max_length, end - start + 1)
            
        return max_length
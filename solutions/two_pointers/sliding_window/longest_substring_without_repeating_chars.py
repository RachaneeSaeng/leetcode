# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# https://algo.monster/problems/longest_substring_without_repeating_characters

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0
        n = len(s)
        i, j = 0,0
        char_set = set()
        while i <= j and j < n:
            new_char = s[j]            
            if new_char in char_set:
                # move i until pass the repeatign char
                while True:
                    c =  s[i]                   
                    char_set.remove(c)
                    i += 1
                    if c == new_char:
                        break          
            else: 
                sub_str = s[i:j+1]
                if  len(sub_str) > longest_substr:
                    longest_substr = len(sub_str)
                    
            j += 1
            char_set.add(new_char)
                
        return longest_substr
# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter

# if one of s1's permutations is the substring of s2.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_len])
        last_posible_start = s2_len - s1_len
        
        for i in range(last_posible_start + 1):
            if s1_counter == s2_counter:
                return True
            if i < last_posible_start:
                s2_counter[s2[i + s1_len]] += 1
                s2_counter[s2[i]] -= 1
                
        return False
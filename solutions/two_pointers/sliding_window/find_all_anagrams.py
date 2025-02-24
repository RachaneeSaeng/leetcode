# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# https://algo.monster/problems/find_all_anagrams

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])
        last_posible_start = s_len - p_len
        
        result = []
        
        for i in range(last_posible_start + 1):
            if s_counter == p_counter:
                result.append(i)
            if i < last_posible_start:
                s_counter[s[i + p_len]] += 1
                s_counter[s[i]] -= 1
                
        return result        
        
        
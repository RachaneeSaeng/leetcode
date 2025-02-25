# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

import sys
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        char_positions = {}
        min_length = sys.maxsize
        
        for i, c in enumerate(cards):
            if c in char_positions:
                lenght = i - char_positions[c] + 1
                min_length = min(min_length, lenght)
                
            char_positions[c] = i
        
        if min_length == sys.maxsize:
            return -1
        else:
            return min_length
# https://algo.monster/problems/binary-search-speedrun?questionIndex=1
# https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil
from typing import List

# time complexity: O(nlog(max(piles)))
# space complexity: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish_eating(piles, h, k):
            hours_used = 0
            for p in piles:
                hours_used += ceil(float(p)/k)
            return hours_used <= h

        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            mid = (left + right) // 2
            if can_finish_eating(piles, h, mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return min_speed
        
    
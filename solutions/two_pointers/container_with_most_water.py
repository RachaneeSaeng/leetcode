# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,n-1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            max_area = max(max_area, area)
            
            # move the pointer with the smaller height first just in case we can find a taller height, potentially increasing the area
            # WHY we move pointer with the lower height (either i or j)??
            # because we already have the max area with that height as the left or right of container - 
            # since it is the lower pointer that means that every other distance that is closer will always be a smaller distance with the same or less height which means smaller area. 
            # Therefore we do not need to look at every other combinations having that height as the left or right line.
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
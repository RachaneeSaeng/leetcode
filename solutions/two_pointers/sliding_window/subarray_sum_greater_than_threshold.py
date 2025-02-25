# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[0:k-1])        
        result = 0
        for i in range(len(arr)-k+1):
            window_sum += arr[i + k-1]
            if window_sum // k >= threshold:
                result += 1
            window_sum -= arr[i]
        
        return result
            
# https://algo.monster/problems/subarray_sum_fixed
from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> int:
        window_sum = 0
        max_sum = 0
        
        for i in range(len(nums)):
            window_sum += nums[i]
            if i + 1 >= k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[i + 1 - k]
                
        return max_sum
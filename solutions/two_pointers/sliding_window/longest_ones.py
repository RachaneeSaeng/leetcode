# https://leetcode.com/problems/max-consecutive-ones-iii/description/

from typing import List

# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# OR, the maximum length of a subarray with at most k 0's.

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_length = 0
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            
            if zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            
            max_length = max(max_length, i - start + 1)
            
        return max_length
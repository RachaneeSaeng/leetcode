# https://leetcode.com/problems/subarray-sum-equals-k/description/?envType=problem-list-v2&envId=prefix-sum

# sum of a subarray [i, j] is equal to the sum of [0, j] minus the sum of [0, i - 1].

from typing import List

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        prefix_sum_map = {}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            if prefix_sum == k:
                result += 1
                
            prefix_sum_complement = prefix_sum -  k
            if prefix_sum_complement in prefix_sum_map:
                result += 1
                
            prefix_sum_map[prefix_sum] = i
                
        return result
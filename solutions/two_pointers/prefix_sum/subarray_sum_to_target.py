# https://leetcode.com/problems/subarray-sum-equals-k/description/?envType=problem-list-v2&envId=prefix-sum

# sum of a subarray [i, j] is equal to the sum of [0, j] minus the sum of [0, i - 1].

from typing import List

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        prefix_sum_count = {}
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum == k:
                result += 1
                
            prefix_sum_complement = prefix_sum -  k
            if prefix_sum_complement in prefix_sum_count:
                result += prefix_sum_count[prefix_sum_complement]
                
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1
                
        return result
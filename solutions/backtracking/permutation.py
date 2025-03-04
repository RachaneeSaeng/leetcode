# https://leetcode.com/problems/permutations/description/

from typing import List

# Time complexity: O(n!)
# Space complexity: O(n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        def backtrack(start):
            
            if start == n: # got a permutation to add to the result
                result.append(nums[:])
                return
            
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result
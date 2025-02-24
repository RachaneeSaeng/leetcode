# https://leetcode.com/problems/contains-duplicate/description/

from typing import List

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_positions = {}
        for num in nums:
            if num in num_positions:
                return True
            num_positions[num] = True
        return False
    
    # class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     if len(set(nums)) == len(nums):
    #         return False
    #     else:
    #         return True 
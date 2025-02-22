# https://leetcode.com/problems/move-zeroes/description/
# https://algo.monster/problems/move_zeros

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        latest_non_zero = -1
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num != 0:                
                nums[i] = 0
                latest_non_zero += 1
                nums[latest_non_zero] = num
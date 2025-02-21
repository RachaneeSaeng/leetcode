# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
                
            if nums[mid] == nums[mid + 1]: # this will tell the the numbers still have paring pattern
                left = mid + 2
            else:
                right = mid
                
        return nums[left]
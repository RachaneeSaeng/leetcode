# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# https://algo.monster/problems/min_in_rotated_sorted_array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
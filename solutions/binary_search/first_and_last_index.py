# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

# time complexity: O(log(n))
# space complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        first_occurance_idx = -1
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
                first_occurance_idx = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        lest_occurance_idx = -1
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
                lest_occurance_idx = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [first_occurance_idx, lest_occurance_idx]
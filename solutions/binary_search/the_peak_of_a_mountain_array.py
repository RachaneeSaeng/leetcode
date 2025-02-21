# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# https://algo.monster/problems/peak_of_mountain_array

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                right = mid -1
        return left  
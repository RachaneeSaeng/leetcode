# https://algo.monster/problems/binary_search_duplicates

from typing import List

# time complexity: O(log(n))
# space complexity: O(1)
class Solution:
    def findFirstOccurance(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n-1
        first_occurance_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == k:
                right = mid - 1
                first_occurance_idx = mid
            elif arr[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
                
        return first_occurance_idx
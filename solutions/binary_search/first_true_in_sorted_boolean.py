# https://algo.monster/problems/binary_search_boundary

from typing import List

# time complexity: O(log(n))
# space complexity: O(1)
class Solution:
    def findFirstTrue(self, arr: List[bool]) -> int:
        n = len(arr)
        left, right = 0, n-1
        first_true_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid]:
                right = mid - 1
                first_true_idx = mid
            else:
                left = mid + 1
                
        return first_true_idx
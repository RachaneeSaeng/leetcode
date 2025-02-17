# https://leetcode.com/problems/find-k-closest-elements/
# https://algo.monster/liteproblems/658

from typing import List

# time complexity: O(log(n - k) + k)
# space complexity: O(k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def findStartingIndex(arr: List[int], k: int, x: int) -> int:
            n = len(arr)
            left, right = 0, n - k
            while left < right:
                mid = (left + right) // 2
                # Check the distance from the x to the middle element and the element at mid + k position.
                # If the element at mid is closer to x or equal in distance compared to the element at mid + k,
                # we move the right pointer to mid. Otherwise, we adjust the left pointer to mid + 1.
                if x - arr[mid] <= arr[mid + k] - x:
                    right = mid
                else:
                    left = mid + 1        
            return left
    
        starting_index = findStartingIndex(arr, k, x)
        return arr[starting_index:starting_index + k]
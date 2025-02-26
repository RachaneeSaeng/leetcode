# https://leetcode.com/problems/product-of-array-except-self/description/
# https://algo.monster/problems/product_of_array_except_self

from typing import List

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        right = 1
        
        # store prefix product in left and suffix product in right
        # store use two pointers that move in opposite direction to put the prefix product and suffix product into result
        for i in range(n):
            result[i] *= left 
            left *= nums[i]
            
            j = n - i - 1
            result[j] *= right
            right *= nums[j]
            
        return result       
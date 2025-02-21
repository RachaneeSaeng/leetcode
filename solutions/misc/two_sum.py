# https://leetcode.com/problems/two-sum/description/
from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_positions = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_positions:
                return [num_positions[complement], i]
            num_positions[num] = i
        return []

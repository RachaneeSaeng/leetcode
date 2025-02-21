# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# https://algo.monster/problems/two_sum_sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            
            if sum > target:
                j -= 1
            else:
                i += 1
                
        return [-1, -1]
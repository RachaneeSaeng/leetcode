# https://leetcode.com/problems/range-sum-query-immutable/description/
# https://algo.monster/problems/range_sum_query_immutable

from typing import List

# time complexity: O(n), space complexity: O(1)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# https://leetcode.com/problems/top-k-frequent-elements/description/
# https://algo.monster/liteproblems/347

from typing import List, Counter
import heapq

# Time complexity: O(nlogk)
# Space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        
        heap = []
        for number, count in num_counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, number))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, number))

        return [item[1] for item in heap]
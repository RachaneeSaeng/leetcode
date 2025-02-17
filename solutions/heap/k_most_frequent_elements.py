# https://leetcode.com/problems/top-k-frequent-elements/description/
# https://algo.monster/liteproblems/347

from typing import List
import heapq

# Time complexity: O(nlogk)
# Space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        heap = []
        result = []
        
        for num in nums:
            count = num_counts.get(num, 0) 
            count += 1
            num_counts[num] = count
        
        for number, count in num_counts.items():            
            if len(heap) < k:
                heapq.heappush(heap, (count, number))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, number))
        
        for _ in range(k):
            count, number = heapq.heappop(heap)
            result.append(number)
                  
        return result
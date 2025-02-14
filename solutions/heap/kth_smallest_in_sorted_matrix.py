# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# https://algo.monster/problems/kth_smallest_element_in_a_sorted_matrix
import heapq
from typing import List

# time complexity: O(k * log(n))
# space complexity: O(n)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = [(matrix[i][0], i, 0) for i in range(min(n, k))] # save tuple (min_number, row, col) for the first element of each row
        heapq.heapify(min_heap)
        
        for _ in range(k-1):
            min_number, current_row, current_col = heapq.heappop(min_heap)
            if current_col + 1 < n:
                heapq.heappush(min_heap, (matrix[current_row][current_col + 1], current_row, current_col + 1))
            
        return heapq.heappop(min_heap)[0]
    
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     n = len(matrix)
    #     min_heap = [(matrix[i][0], i, 0) for i in range(min(n, k))] # save tuple (min_number, row, col) for the first element of each row
    #     heapq.heapify(min_heap)
        
    #     for _ in range(k-1):
    #         min_number, current_row, current_col = heapq.heappop(min_heap)
    #         if current_col + 1 < n:
    #             heapq.heappush(min_heap, (matrix[current_row][current_col + 1], current_row, current_col + 1))
            
    #     return heapq.heappop(min_heap)[0]
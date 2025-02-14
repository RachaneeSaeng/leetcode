# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# https://algo.monster/problems/kth_smallest_element_in_a_sorted_matrix
import heapq
from typing import List

# time complexity: O(k * log(n))
# space complexity: O(n)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = [(matrix[0][0], 0, 0)] # save tuple (min_number, rol, col) for the first element
        
        for _ in range(k-1):
            min_number, current_row, current_col  = heapq.heappop(min_heap)
            next_row = current_row + 1 # pointer move relatively to the current smallest element
            next_col = current_col + 1
            
            if current_col == 0 and next_row < n: # add only first element of the next row to heap so it be consider as the next smallest element 
                heapq.heappush(min_heap, (matrix[next_row][current_col], next_row, current_col))
            if next_col < n:
                heapq.heappush(min_heap, (matrix[current_row][next_col], current_row, next_col))
            
        return heapq.heappop(min_heap)[0]
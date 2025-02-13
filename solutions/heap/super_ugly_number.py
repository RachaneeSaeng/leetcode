import heapq
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        min_heap = [1]
        current_ugly_number = 0
        max_int_value = (1 << 31) - 1
        
        for _ in range(n):
            current_ugly_number = heapq.heappop(min_heap)
            
            while min_heap and current_ugly_number == min_heap[0]: # Skip duplicates
                heapq.heappop(min_heap)
                
            for prime in primes:
                next_ugly_number = current_ugly_number * prime
                if next_ugly_number <= max_int_value:
                    heapq.heappush(min_heap, next_ugly_number) # The library heapq is a min heap as default
                    
        return current_ugly_number
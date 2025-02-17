# https://leetcode.com/problems/top-k-frequent-words/
# https://algo.monster/problems/top_k_frequently_mentioned_keywords

from typing import Counter, List, Tuple
import heapq

# time complexity: O(nlogk)
# space complexity: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)

        heap = []
        for word, count in word_counts.items():           
            heapq.heappush(heap, (count, RevrseValue(word)))
            if len(heap) > k:
                heapq.heappop(heap) # if there are multiple words with the same frequency, the word with higher value will be popped first (z will be popped before a)
              
        res = []
        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1].value)
            
        return res[::-1]
    
class RevrseValue:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value # to make word with higher value less than word with lower value
# https://leetcode.com/problems/top-k-frequent-words/
# https://algo.monster/problems/top_k_frequently_mentioned_keywords

from typing import List
import heapq

# time complexity: O(n * log(n))
# space complexity: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        heap = []
        for word, count in word_counts.items():           
            heapq.heappush(heap, (-count, word))
              
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1]) # words with the same frequency are ordered alphabetically when they are popped from the heap
            
        return result
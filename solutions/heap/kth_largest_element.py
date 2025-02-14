# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List

# time complexity: O(n + k log n) or O(n log n)
#pace complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:  
        # time complexity: O(log n)      
        def heapify(nums, n, i):
            largest_index = i
            left = 2 * i + 1 # left node
            right = 2 * i + 2 # right node

            if left < n and nums[largest_index] < nums[left]:
                largest_index = left

            if right < n and nums[largest_index] < nums[right]:
                largest_index = right

            if largest_index != i:
                nums[i], nums[largest_index] = nums[largest_index], nums[i]
                heapify(nums, n, largest_index)


        n = len(nums)
        middle_index = n // 2 - 1
        last_index = n - 1
        target_index = n - k -1

        for i in range(middle_index, -1, -1):
            heapify(nums, n, i)

        for remain_array_len in range(last_index, target_index, -1):
            nums[0], nums[remain_array_len] = nums[remain_array_len], nums[0]
            heapify(nums, remain_array_len, 0)

        return nums[n - k]
    

# # time complexity: O(n * log(k)) or O(n log n)
# # space complexity: O(k)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         # Create a min-heap with the first k elements
#         heap = nums[:k]
#         heapq.heapify(heap)
        
#         # Iterate through the rest of the elements
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heappushpop(heap, num)
        
#         # The root of the heap is the kth largest element
#         return heap[0] # the root of the heap is the smallest element among k items, which = kth largest element
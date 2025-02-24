# https://algo.monster/problems/linked_list_cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from solutions.two_pointers.list_node import ListNode

# time complexity: O(n)
# space complexity: O(1)
# Not: this can be solved by using a hash table to store visited nodes but the space complexity will be O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
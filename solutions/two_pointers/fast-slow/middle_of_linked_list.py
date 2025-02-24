# https://leetcode.com/problems/middle-of-the-linked-list/description/
# https://algo.monster/problems/middle_of_linked_list

from typing import Optional

from solutions.two_pointers.list_node import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        # if fast reach the last node, the slow node will reach the middle one
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
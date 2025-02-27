# https://leetcode.com/problems/binary-tree-right-side-view/description/

from typing import Optional, List
from solutions.tree.tree_node import TreeNode
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        while queue:
            node = TreeNode()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                     
            result.append(node.val) # append only last node in the level
                
        return result
# https://leetcode.com/problems/binary-tree-right-side-view/description/

from typing import Optional, List
from solutions.graph.tree_node import TreeNode
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                
                # Key trick: only add the last node in the current level
                if i == level_length - 1:
                    result.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result      
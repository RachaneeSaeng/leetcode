# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# https://algo.monster/problems/binary_tree_level_order_traversal

from typing import List, Optional
from solutions.tree.tree_node import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_nodes = []
            for _ in range(len(queue)): # process all nodes in the current level
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)   
            
        return result    
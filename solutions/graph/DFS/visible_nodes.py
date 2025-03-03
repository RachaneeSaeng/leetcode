# https://algo.monster/problems/visible_tree_node

# a node is labeled as "visible" if, on the path from the root to that node, there isn't any node with a value higher than this node's value
from typing import List, Optional

from solutions.graph.tree_node import TreeNode

class Solution:    
    def countVisibleNodes(self, root: Optional[TreeNode], parentVal: int | None = None) -> int:
        if root is None:
            return 0
        
        if not parentVal or parentVal <= root.val:
            return 1 + self.countVisibleNodes(root.right, root.val) + self.countVisibleNodes(root.right, root.val) # use devide and conquer to solve the problem
        
        return 0
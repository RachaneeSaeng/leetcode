# https://algo.monster/problems/invert_binary_tree
# https://leetcode.com/problems/invert-binary-tree/description/

from typing import Optional

from solutions.graph.tree_node import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        
        return root
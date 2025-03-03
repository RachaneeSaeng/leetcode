# https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional

from solutions.graph.tree_node import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            
            # For the left subtree, the upper bound is updated to the current node's value, as all values in the left subtree must be less than the current node's value
            # For the right subtree, the lower bound is updated to the current node's value, as all values in the right subtree must be greater than the current node's value
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        
        return dfs(root, None, None)
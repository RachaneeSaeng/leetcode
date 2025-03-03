# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
# https://algo.monster/problems/insert_into_bst

from typing import Optional

from solutions.graph.tree_node import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
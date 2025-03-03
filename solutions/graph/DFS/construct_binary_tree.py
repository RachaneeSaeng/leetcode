# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

from typing import List, Optional

from solutions.graph.tree_node import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # This index helps to determine the boundary between the left and right subtrees in the inorder list
        # In another word, root_index tell number of nodes in the left subtree
        root_index = inorder.index(root_val)
        
        root.left = self.buildTree(preorder[1:1+root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])
        
        return root
        
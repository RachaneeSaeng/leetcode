# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# https://algo.monster/problems/lowest_common_ancestor_on_bst


from solutions.graph.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
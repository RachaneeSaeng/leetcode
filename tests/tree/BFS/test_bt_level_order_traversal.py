import pytest
from solutions.tree.tree_node import TreeNode
from solutions.tree.BFS.bt_level_order_traversal import Solution

def test_level_order_empty_tree():
    solution = Solution()
    assert solution.levelOrder(None) == []

def test_level_order_single_node():
    solution = Solution()
    root = TreeNode(1)
    assert solution.levelOrder(root) == [[1]]

def test_level_order_multiple_levels():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.levelOrder(root) == [[1], [2, 3], [4, 5, 6, 7]]

def test_level_order_unbalanced_tree():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert solution.levelOrder(root) == [[1], [2], [3], [4]]
    
def test_level_order_unbalanced_tree_2():
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]

if __name__ == "__main__":
    pytest.main()
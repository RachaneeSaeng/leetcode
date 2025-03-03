import pytest
from solutions.graph.tree_node import TreeNode
from solutions.graph.DFS.visible_nodes import Solution

def test_countVisibleNodes_single_node():
    root = TreeNode(1)
    sol = Solution()
    assert sol.countVisibleNodes(root) == 1

def test_countVisibleNodes_all_visible():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    sol = Solution()
    assert sol.countVisibleNodes(root) == 3

def test_countVisibleNodes_none_visible():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    sol = Solution()
    assert sol.countVisibleNodes(root) == 1

def test_countVisibleNodes_mixed_visibility():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(4)
    sol = Solution()
    assert sol.countVisibleNodes(root) == 3

def test_countVisibleNodes_mixed_visibility_2():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    sol = Solution()
    assert sol.countVisibleNodes(root) == 3

def test_countVisibleNodes_empty_tree():
    root = None
    sol = Solution()
    assert sol.countVisibleNodes(root) == 0

if __name__ == "__main__":
    pytest.main()
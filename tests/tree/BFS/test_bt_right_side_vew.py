import pytest
from solutions.tree.tree_node import TreeNode
from solutions.tree.BFS.bt_right_side_view import Solution


def test_right_side_view_empty_tree():
    assert Solution().rightSideView(None) == []

def test_right_side_view_single_node():
    root = TreeNode(1)
    assert Solution().rightSideView(root) == [1]

def test_right_side_view_two_levels():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().rightSideView(root) == [1, 3]

def test_right_side_view_three_levels():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    assert Solution().rightSideView(root) == [1, 3, 4]

def test_right_side_view_left_skewed():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().rightSideView(root) == [1, 2, 3]

def test_right_side_view_right_skewed():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().rightSideView(root) == [1, 2, 3]
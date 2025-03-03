import pytest
from solutions.graph.tree_node import TreeNode
from solutions.graph.BFS.bt_zigzag_level_traversal import Solution

def test_level_order_empty_tree():
    solution = Solution()
    assert solution.zigzagLevelOrder(None) == []

def test_level_order_single_node():
    solution = Solution()
    root = TreeNode(1)
    assert solution.zigzagLevelOrder(root) == [[1]]

def test_level_order_unbalanced_tree_2():
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.zigzagLevelOrder(root) == [[3], [20,9], [15, 7]]
    
def test_level_order_five_levels():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    root.left.left.left.left = TreeNode(16)
    root.left.left.left.right = TreeNode(17)
    root.left.left.right.left = TreeNode(18)
    root.left.left.right.right = TreeNode(19)
    root.left.right.left.left = TreeNode(20)
    root.left.right.left.right = TreeNode(21)
    root.left.right.right.left = TreeNode(22)
    root.left.right.right.right = TreeNode(23)
    root.right.left.left.left = TreeNode(24)
    root.right.left.left.right = TreeNode(25)
    root.right.left.right.left = TreeNode(26)
    root.right.left.right.right = TreeNode(27)
    root.right.right.left.left = TreeNode(28)
    root.right.right.left.right = TreeNode(29)
    root.right.right.right.left = TreeNode(30)
    root.right.right.right.right = TreeNode(31)
    assert solution.zigzagLevelOrder(root) == [
        [1],
        [3, 2],
        [4, 5, 6, 7],
        [15, 14, 13, 12, 11, 10, 9, 8],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    ]

if __name__ == "__main__":
    pytest.main()
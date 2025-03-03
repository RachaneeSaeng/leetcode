import pytest
from solutions.graph.tree_node import TreeNode
from solutions.graph.DFS.valid_binary_search_tree import Solution

def test_valid_bst_case1():
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert sol.isValidBST(root) == True

def test_valid_bst_case2():
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    assert sol.isValidBST(root) == False

def test_valid_bst_case3():
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert sol.isValidBST(root) == False

def test_valid_bst_case4():
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    assert sol.isValidBST(root) == True

def test_valid_bst_case5():
    sol = Solution()
    root = TreeNode(1)
    assert sol.isValidBST(root) == True
    
def test_valid_bst_case6():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    assert sol.isValidBST(root) == False

def test_valid_bst_case7():
    sol = Solution()
    assert sol.isValidBST(None) == True
    
def test_valid_bst_case8():
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    assert sol.isValidBST(root) == False

if __name__ == "__main__":
    pytest.main()
import pytest
from solutions.graph.tree_node import TreeNode
from solutions.graph.DFS.insert_into_binary_search_tree import Solution

def tree_to_list(root):
    """Helper function to convert tree to list (level-order) for easy comparison in tests."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def test_insert_into_bst_empty_tree():
    sol = Solution()
    root = None
    val = 5
    expected = [5]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected

def test_insert_into_bst_one_node():
    sol = Solution()
    root = TreeNode(5)
    val = 3
    expected = [5, 3]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected

def test_insert_into_bst_multiple_nodes_case1():
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    val = 4
    expected = [5, 3, 7, None, 4]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected

def test_insert_into_bst_multiple_nodes_case2():
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    val = 6
    expected = [5, 3, 7, None, None, 6]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected

def test_insert_into_bst_multiple_nodes_case3():
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    val = 8
    expected = [5, 3, 7, None, None, None, 8]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected
    
def test_insert_into_bst_complex_case():
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    val = 5
    expected = [4, 2, 7, 1, 3, 5]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected
    
def test_insert_into_bst_complex_case2():
    sol = Solution()
    root = TreeNode(40)
    root.left = TreeNode(20)
    root.right = TreeNode(60)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(30)
    root.right.left = TreeNode(50)
    root.right.right = TreeNode(70)
    val = 25
    expected = [40, 20, 60, 10, 30, 50, 70, None, None, 25]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected
    
def test_insert_into_bst_given_case():
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    val = 5
    expected = [4, 2, 7, 1, 3, 5]
    assert tree_to_list(sol.insertIntoBST(root, val)) == expected

if __name__ == "__main__":
    pytest.main()
from typing import Optional
import pytest
from solutions.graph.tree_node import TreeNode
from solutions.graph.DFS.invert_binary_tree import Solution

def tree_to_list(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

def list_to_tree(lst: list) -> Optional[TreeNode]:
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

@pytest.mark.parametrize("input_tree, expected_output", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
    ([1, 2], [1, None, 2]),
])
def test_invertTree(input_tree, expected_output):
    solution = Solution()
    root = list_to_tree(input_tree)
    inverted_root = solution.invertTree(root)
    assert tree_to_list(inverted_root) == expected_output
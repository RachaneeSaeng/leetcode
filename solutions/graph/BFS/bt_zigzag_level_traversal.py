# https://algo.monster/problems/binary_tree_zig_zag_traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from collections import deque
from solutions.graph.tree_node import TreeNode
from typing import List, Optional

# time complexity: O(N)
# space complexity: O(N)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        zigzag = False

        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # Key trick: insert the node value at the beginning or the end of the list based on the zigzag flag
                if zigzag:
                    level_nodes.insert(0, node.val)
                else:
                    level_nodes.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(level_nodes)
            zigzag = not zigzag # switch the direction
                  
        return result
            

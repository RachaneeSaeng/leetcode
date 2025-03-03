# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from collections import deque
from typing import Optional

from solutions.graph.tree_node import TreeNode


# time complexity: O(n)
# space complexity: O(n)
class Solution:    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root,1)])
        
        while queue:
            node, depth = queue.popleft()
            
            if not node.left and not node.right:
                return depth
            
            # key trick: store the depth of each node in the queue and +1 when adding children
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
    
    # time complexity: O(n)
    # space complexity: O(n)
    # def maxDepth(self, root: Optional[TreeNode]) -> int:       
    #     if not root:
    #         return 0
        
    #     queue = deque([root])
    #     depth = 0
        
    #     while queue:
    #         for i in range(len(queue)):
    #             node = queue.popleft()
                
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    
    #         # key trick: increment the depth after processing all nodes in the current level               
    #         depth += 1
            
    #     return depth
    
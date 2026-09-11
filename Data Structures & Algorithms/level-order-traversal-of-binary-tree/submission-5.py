# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        return_data = {}

        def traverse(node, level):

            if not node:
                return
            
            return_data[level] = return_data.get(level, []) + [node.val]

            traverse(node.left, level+1)
            traverse(node.right, level+1)

        traverse(root, 0)

        return list(return_data.values())


        """

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        levels = []
        
        def traverse(node: Optional[TreeNode], level: int):
            if not node:
                return
                
            # If we are visiting this depth level for the first time,
            # initialize a new sublist for it
            if len(levels) == level:
                levels.append([])
                
            # Append in-place: O(1) average time complexity
            levels[level].append(node.val)
            
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
            
        traverse(root, 0)
        return levels


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
            
        return result

        
        """
        
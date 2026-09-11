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
        
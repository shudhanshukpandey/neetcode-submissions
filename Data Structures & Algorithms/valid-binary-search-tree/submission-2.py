# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return_data = []

        def inorder(node):

            if not node:
                return
            inorder(node.left)
            return_data.append(node.val)
            inorder(node.right)
        
        inorder(root)
        lst = return_data
        return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))



        
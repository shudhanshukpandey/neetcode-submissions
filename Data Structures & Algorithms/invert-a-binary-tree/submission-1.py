# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node:
                return node
            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)
        
        invert(root)

        return root


    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # Base case: if the tree is empty, return None
#         if not root:
#             return None
        
#         # Recursively invert the left and right subtrees first
#         left_inverted = self.invertTree(root.left)
#         right_inverted = self.invertTree(root.right)
        
#         # Swap the children using the pre-calculated inverted subtrees
#         root.left = right_inverted
#         root.right = left_inverted
        
#         return root


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return None
        
#         # Python evaluates the right side entirely before assigning
#         root.left, root.right = self.invertTree(root.right),        self.invertTree(root.left)
        
#         return root

        
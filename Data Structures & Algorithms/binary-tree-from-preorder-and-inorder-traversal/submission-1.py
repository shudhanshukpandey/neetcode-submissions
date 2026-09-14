# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None

#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
#         return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map value to its index in inorder traversal for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Iterator to keep track of the current root in preorder array
        preorder_iter = iter(preorder)
        
        def helper(left_idx, right_idx):
            # Base case: no elements in this subtree scope
            if left_idx > right_idx:
                return None
            
            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find the split point in inorder array
            mid_idx = inorder_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = helper(left_idx, mid_idx - 1)
            root.right = helper(mid_idx + 1, right_idx)
            
            return root
            
        return helper(0, len(inorder) - 1)

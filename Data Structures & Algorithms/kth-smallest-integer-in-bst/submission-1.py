# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            # 1. Traverse the left subtree
            inorder(node.left)
            
            # 2. Process the current node
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return  # Early exit from this frame
            
            # 3. Traverse the right subtree (only if target hasn't been found)
            if self.result is None:
                inorder(node.right)
                
        inorder(root)
        return self.result

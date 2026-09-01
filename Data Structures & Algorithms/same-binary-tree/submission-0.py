# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are None -> They match structurally
        if not p and not q:
            return True
        
        # Base case 2: Only one node is None -> Structure mismatch
        if not p or not q:
            return False
        
        # Base case 3: Values don't match -> Value mismatch
        if p.val != q.val:
            return False
        
        # Recurse down both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

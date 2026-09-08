class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        
        def inorder(node) -> bool:
            if not node:
                return True
            
            # Check left subtree
            if not inorder(node.left):
                return False
            
            # Check current node
            if node.val <= self.prev:
                return False
            self.prev = node.val
            
            # Check right subtree
            return inorder(node.right)
            
        return inorder(root)

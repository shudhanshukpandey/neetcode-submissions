# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def getlca(node):

            # print(node.val, p.val, q.val)
            

            
            if (p.val<=node.val<=q.val) or (p.val>=node.val>=q.val):
                
                return node
            elif p.val<q.val<node.val or q.val<p.val<node.val:
                
                return getlca(node.left)
            elif p.val>q.val>node.val or q.val>p.val>node.val:
                
                return getlca(node.right)
        
        return getlca(root)
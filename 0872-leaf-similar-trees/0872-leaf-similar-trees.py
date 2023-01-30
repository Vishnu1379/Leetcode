# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        c=[]
        d=[]
        def FirstTree(root1):
            if root1 == None:
                return None
            if root1.left == None and root1.right == None:
                c.append(root1.val)
            FirstTree(root1.left)
            FirstTree(root1.right)
        def SecondTree(root2):
            if root2==None:
                return None
            if root2.left==None and root2.right==None:
                d.append(root2.val)
            SecondTree(root2.left)
            SecondTree(root2.right)
        FirstTree(root1)
        SecondTree(root2)
        if c==d:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
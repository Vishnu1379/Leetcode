# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        c1=[]
        c2=[]
        def inorder(root1):
            if root1:
                inorder(root1.left)
                c1.append(root1.val)
                inorder(root1.right)
        def inorder(root1):
            if root1:
                inorder(root1.left)
                c2.append(root1.val)
                inorder(root1.right)
        inorder(root1)
        inorder(root2)
        return sorted(c1+c2)
        
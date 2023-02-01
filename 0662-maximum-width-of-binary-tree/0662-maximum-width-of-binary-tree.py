# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=[(root,0)]
        width=1
        while len(q)!=0:
            if len(q)>1:
                width=max(width,q[-1][1]-q[0][1]+1)
            temp=[]
            while len(q)!=0:
                node,pos=q.pop(0)
                if node.left:
                    temp.append((node.left,pos*2))
                if node.right:
                    temp.append((node.right,pos*2+1))
            q=temp
        return width
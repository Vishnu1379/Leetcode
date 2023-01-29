# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        stack=[root]
        direction=1
        while stack:
            level=[]
            for i in range(len(stack)):
                node=stack.pop(0)
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if direction % 2==0:
                res.append(level[::-1])
            else:
                res.append(level)
            direction+=1 
        return res
            
        
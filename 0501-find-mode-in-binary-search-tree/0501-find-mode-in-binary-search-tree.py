# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        c=[]
        def dfs_element_freq(root):
            if root is None:
                return None
            if root.val  not in d:
                d[root.val]=1
            else:
                d[root.val]+=1
            dfs_element_freq(root.left)
            dfs_element_freq(root.right)
            
        dfs_element_freq(root)
        k=max(d.values())
        for i,j in d.items():
            if j==k:
                c.append(i)
        return c
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q=[root]
        ans=[]
        while q:
            temp=[]
            for i in range(len(q)):
                top=q.pop(0)
                temp.append(top.val)
                q.extend(top.children)
            ans.append(temp)
        return ans
        
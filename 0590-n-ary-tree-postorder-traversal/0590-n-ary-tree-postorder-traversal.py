"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack=[root]
        ans=[]
        while len(stack):
            top=stack.pop()
            ans.append(top.val)
            stack.extend(top.children or [])
        return ans[::-1]
            
        
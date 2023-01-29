# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1:
            return t2
        if not t2:
            return t1
        stack = [(t1, t2)]
        while stack:
            node1, node2 = stack.pop()
            node1.val += node2.val
            if node1.right and node2.right:
                stack.append((node1.right, node2.right))
            elif node2.right:
                node1.right = node2.right
            if node1.left and node2.left:
                stack.append((node1.left, node2.left))
            elif node2.left:
                node1.left = node2.left
        return t1
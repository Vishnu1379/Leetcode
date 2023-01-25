# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.function(root,ans)
        return ans
    def function(self,root,ans):
        if root:
            ans.append(root.val)
            self.function(root.left,ans)
            self.function(root.right,ans)
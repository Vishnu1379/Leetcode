# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        inorderlist=inorder(root)
        ans=temp=TreeNode(inorderlist[0])
        for i in range(1,len(inorderlist)):
            temp.right=TreeNode(inorderlist[i])
            temp=temp.right
        return ans
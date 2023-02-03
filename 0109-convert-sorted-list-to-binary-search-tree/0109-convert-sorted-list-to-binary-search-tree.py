# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def make(self,A):
        if A:
            m=len(A)//2
            n=TreeNode(A[m])
            n.left=self.make(A[:m])
            n.right=self.make(A[m+1:])
            return n
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        c=[]
        curr=head
        while curr:
            c.append(curr.val)
            curr=curr.next
        return self.make(c)
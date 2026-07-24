# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        post = head

        while post is not None and post.next is not None:
            pre = pre.next
            post = post.next.next

        return pre    
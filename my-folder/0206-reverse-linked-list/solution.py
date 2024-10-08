# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        temp = None
        curr = head
        nxt = head

        while curr:
            nxt = curr.next
            curr.next = temp
            temp = curr
            curr = nxt

        return temp



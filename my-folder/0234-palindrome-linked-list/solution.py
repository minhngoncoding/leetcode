# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = head
        fast = head

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        first_half = []
        second_half = []
        while middle:
            first_half.append(head.val)
            second_half.append(middle.val)
            head = head.next
            middle = middle.next

        return True if first_half == second_half[::-1] else False
            
        

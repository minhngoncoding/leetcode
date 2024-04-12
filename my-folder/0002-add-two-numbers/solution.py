# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = ""
        num2 = ""
        result = ListNode()
        head = result
        saving = 0
        while l1 or l2 or saving != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2

            real_total = total+saving

            value = real_total % 10 if real_total >= 10 else real_total
            temp = ListNode(value)
            head.next = temp

            saving = 0 if real_total < 10 else 1


            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            head = head.next
        return result.next

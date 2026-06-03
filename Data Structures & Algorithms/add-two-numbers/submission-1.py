# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 and l2:
            sum_v = l1.val + l2.val + carry
            l1.val = (sum_v) % 10
            carry = 1 if sum_v > 9 else 0
            dummy.next = l1
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        while l1:
            sum_v = l1.val + carry
            l1.val = sum_v % 10
            carry = 1 if sum_v > 9 else 0
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next
        
        while l2:
            sum_v = l2.val + carry
            l2.val = sum_v % 10
            carry = 1 if sum_v > 9 else 0
            dummy.next = l2
            l2 = l2.next
            dummy = dummy.next
            
        if carry > 0:
            dummy.next = ListNode(1)
        return head.next
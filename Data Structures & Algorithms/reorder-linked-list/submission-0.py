# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def print_list(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        middle, end = head, head

        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        # separate into two lists
        second_half = middle.next
        middle.next = None

        # reverse the second half
        second_half = self.reverseList(second_half)
        
        # sentinel node
        dummy = ListNode(-1)
        first_half = head

        # add nodes switching between the two lists
        it = 0
        while first_half and second_half:
            if it % 2 == 0:
                dummy.next = first_half
                first_half = first_half.next
            else:
                dummy.next = second_half
                second_half = second_half.next
            dummy = dummy.next
            it += 1
        
        # add if not exhausted
        if first_half:
            dummy.next = first_half
        if second_half:
            dummy.next = second_half

        # head = dummy.next
        return
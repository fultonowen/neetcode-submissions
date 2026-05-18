# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head

        curr = head
        for i in range(n):
            curr = curr.next
        
        previous_node = None
        removal_node = head

        while curr:
            previous_node = removal_node
            removal_node = removal_node.next
            curr = curr.next
        
        print(removal_node.val)
        
        if previous_node == None: return head.next

        previous_node.next = removal_node.next
        return head
        
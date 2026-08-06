# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Divide the list into two halves
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # Reverse the head2
        prev = None
        cur = head2

        while cur != None:
            # Always store the pointer which will be modified next
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # Merge the head2 with head1
        head1 = head
        head2 = prev
        while head2 != None:
            # Always store the pointer which will be modified next
            h1_next = head1.next
            h2_next = head2.next

            head1.next = head2
            head2.next = h1_next
            
            head1 = h1_next
            head2 = h2_next

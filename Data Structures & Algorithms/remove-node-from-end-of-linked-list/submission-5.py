# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        tmp = head

        while tmp and n > 0:
            tmp = tmp.next
            n -= 1

        print(tmp, n)

        if tmp == None and n == 0:
            return head.next
        
        tmp_head = head
        while tmp != None:
            prev = tmp_head
            tmp_head = tmp_head.next
            tmp = tmp.next

        # tmp_head points to the nth node
        if prev:
            prev.next = tmp_head.next
        else:
            head = head.next

        return head
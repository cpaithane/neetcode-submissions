# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_sublist(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        prev = None
        cur = head

        while cur != None:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        print("Cur ", cur)
        return (prev, head)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res_head = None
        nodes = 0
        s_head = s_end = None
        prev_s_tail = None

        while head != None:
            # Form a sub linked list
            s_head = head
            while nodes < k and head != None:
                s_end = head
                head = head.next
                nodes += 1

            # Check if the sublist has exactly k nodes
            if nodes == k:
                if res_head == None:
                    res_head = s_end

                print("Before", s_head.val, s_end.val)
                s_end.next = None
                s_head, s_end = self.reverse_sublist(s_head, s_end)
                print("After", s_head.val, s_end.val)
            else:
                if res_head == None:
                    res_head = s_head

            # Join the reversed sublist to next
            if prev_s_tail != None:
                prev_s_tail.next = s_head

            prev_s_tail = s_end
            nodes = 0

        return res_head
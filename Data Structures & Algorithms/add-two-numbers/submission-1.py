# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        end = sum_list = None

        # Traverse both lists till one of them is exhausted.
        while l1 or l2 or carry > 0:
            addition = carry
            if l1:
                addition += l1.val
                l1 = l1.next

            if l2:
                addition += l2.val
                l2 = l2.next

            carry = addition // 10
            addition = addition % 10

            sum_node = ListNode(addition, None)
            if sum_list == None:
                end = sum_list = sum_node
            else:
                end.next = sum_node
                end = end.next

        return sum_list

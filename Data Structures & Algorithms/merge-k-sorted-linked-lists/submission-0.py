# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeSortedLists(self, list1: List[ListNode], list2: List[ListNode]) -> ListNode:
        res_head = res_end = None

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        while list1 != None and list2 != None:
            node = None
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            
            if res_head == None:
                res_head = res_end = node
            else:
                res_end.next = node
                res_end = res_end.next

        if list1 != None:
            res_end.next = list1
        else:
            res_end.next = list2

        return res_head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_head = None

        for i, l in enumerate(lists):
            res_head = self.mergeSortedLists(res_head, l)

        return res_head
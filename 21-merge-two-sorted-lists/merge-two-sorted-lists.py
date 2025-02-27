# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        l2 = []
        head = ListNode()
        if not list1 and not list2:
            return head.next
        while list1:
            l1.append(list1.val)
            list1 = list1.next
        while list2:
            l2.append(list2.val)
            list2 = list2.next
        print(l1)
        print(l2)
        result = sorted(l1+l2)
        print(result)

        head = ListNode(result[0])
        current = head

        for x in result[1:]:
            current.next = ListNode(x)
            current = current.next

        return head
        
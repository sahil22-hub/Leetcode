# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0,head)
        left, right = temp, head
        while right:
            if right.next and right.val == right.next.val:
                while right.next and right.val == right.next.val:
                    right = right.next
                left.next = right.next
            else:
                left = left.next
            right = right.next
        print(temp.next)
        return temp.next

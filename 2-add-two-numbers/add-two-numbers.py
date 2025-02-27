from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = l1, l2
        x, y = "", ""

        # Extract numbers from linked lists
        while temp1:
            x += str(temp1.val)
            temp1 = temp1.next
        while temp2:
            y += str(temp2.val)
            temp2 = temp2.next

        # Reverse, add, and reverse back
        z = str(int(x[::-1]) + int(y[::-1]))[::-1]

        # Create new linked list
        head = ListNode(int(z[0]))  # First node
        current = head

        for digit in z[1:]:
            current.next = ListNode(int(digit))  # Create new node
            current = current.next  # Move to next node

        return head  # Return head of the new linked list

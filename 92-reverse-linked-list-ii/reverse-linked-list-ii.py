# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head  # No change needed

        dummy = ListNode(0)  # Dummy node before head
        dummy.next = head
        prev = dummy
        curr = head
        count = 1  # 1-based indexing

        # Step 1: Move `prev` to the node before `left`
        while count < left:
            prev = curr
            curr = curr.next
            count += 1

        # Step 2: Reverse the sublist from `left` to `right`
        temp_before_left = prev  # Store the node before `left`
        temp_left = curr  # Store `left` node (start of reversal)
        prev = None

        for _ in range(right - left + 1):
            nxt = curr.next  # Store next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev forward
            curr = nxt  # Move curr forward

        # Step 3: Reconnect the reversed sublist
        temp_before_left.next = prev  # Connect node before `left` to new reversed head
        temp_left.next = curr  # Connect tail of reversed list to the remaining part

        return dummy.next if left != 1 else prev  # Return new head if left == 1





            


            
        
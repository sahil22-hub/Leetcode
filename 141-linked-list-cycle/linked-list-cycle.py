# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next           # Move slow by 1 step
            fast = fast.next.next      # Move fast by 2 steps
            
            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle
                

        
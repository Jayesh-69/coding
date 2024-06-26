# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the resulting list
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Value of l1, or 0 if l1 is None
            val2 = l2.val if l2 else 0  # Value of l2, or 0 if l2 is None
            total = val1 + val2 + carry  # Sum of the values and carry
            
            carry = total // 10  # Update carry
            remainder = total % 10  # Remainder to store in the node
            
            current.next = ListNode(remainder)  # Create a new node with the remainder
            current = current.next  # Move to the next node
            
            # Move to the next nodes in l1 and l2, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  # Return the next node of the dummy, which is the head of the result list

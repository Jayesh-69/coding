# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the lengths of both linked lists
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lengthA = getLength(headA)
        lengthB = getLength(headB)
        
        # Align the start of both linked lists
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1
        
        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1
        
        # Traverse both lists together to find the intersection node
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the lengths of both linked lists
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lengthA = getLength(headA)
        lengthB = getLength(headB)
        
        # Align the start of both linked lists
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1
        
        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1
        
        # Traverse both lists together to find the intersection node
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
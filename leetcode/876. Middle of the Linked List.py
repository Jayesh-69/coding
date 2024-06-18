# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oneCounter = head
        another = head

        while another and another.next:
            oneCounter = oneCounter.next
            another = another.next.next
        return oneCounter
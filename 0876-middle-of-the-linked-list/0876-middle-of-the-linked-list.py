# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast !=  None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # this loop will break when fast reaches the end of linked list 
        # and slow is half of fast so slow must be at middle of linked list
        return slow
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Move slow 1 step and fast 2 steps if they meet, a cycle exists
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # cycle exist

                slow = head # Move slow back to the head

                # Move both 1 step at a time they will meet at the START of the cycle
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                # The meeting node is the start of the cycle
                return slow

        # fast reached the end, so there is no cycle
        return None
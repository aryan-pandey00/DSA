class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
         
        # Treat nums like a linked list:  index → nums[index]

        while True:
            slow = nums[slow]  # slow moves one step at a time
            fast = nums[fast]  # fast moves 2 step at a time
            fast = nums[fast]

            if slow == fast : # when cycle is identified
                slow = 0
                 
                # Move both 1 step at a time
                # They meet at the start of the cycle = duplicate number
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]

                return slow 
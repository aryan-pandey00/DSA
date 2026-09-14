class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.getNext(slow) # slow move once 
            fast = self.getNext(fast) # fast move twice
            fast = self.getNext(fast)

            if slow == fast:
                return slow ==1  # check slow is equal to 1 or not and then return true or false

    # function to find next step by squaring and adding digits
    def getNext(self,n): 

        total = 0

        while n>0:
            digit = n%10
            total +=digit*digit
            n//=10

        return total
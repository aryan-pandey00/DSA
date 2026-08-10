class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else: # it is for exception when input is 9 ending numbers like 29,39,199 
                digits[i] = 0
        return [1] + digits

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        high = 0
        low = 0
        zero = 0 # store number of zeros
        result = 0

        for high in range(len(nums)):
            if nums[high] == 0:#checking for zero and if zero found increase the value of zero
                zero+=1

            while zero >k:#replacement more than k then shrink window
                if nums[low] == 0:
                    zero-=1
                low +=1

            length = high - low +1
            result = max(result,length)

        return result 

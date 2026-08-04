class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        sum = 0
        min_result = float('inf')#initially set infinity so can be replaced by any small value

        while (high < len(nums)):
            sum = sum + nums[high]

            while(sum >= target):
                result = high-low+1
                min_result = min(min_result,result)

                sum = sum - nums[low]
                low +=1

            high +=1

        if min_result == float('inf'): # if no any subarray is found who meet target return 0
            return 0

        else:
            return min_result


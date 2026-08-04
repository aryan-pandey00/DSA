class Solution:
    def maxSubarraySum(self, arr, k):
        
        if len(arr) < k:
            return 0
            
        low = 0
        high = k-1
        
        sum = 0
        max_sum = 0
        
        for i in range (low, high+1):
            sum = sum + arr[i]
            
        while (high<len(arr)):
            max_sum = max(max_sum,sum)
            
            if high == len(arr) - 1:# this is checking does the next window exist or not
                break
            
            sum = sum - arr[low] + arr[high+1] # high + 1 because high is not updated yet
            
            low +=1
            high +=1
            
        return max_sum
        

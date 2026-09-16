class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        best_ending = arr[0]
        ans = arr[0]
        
        for i in range (1,len(arr)):
            v1 = best_ending + arr[i]
            v2 = arr[i]
            
            best_ending = min(v1,v2)
            ans = min(ans,best_ending)
            
        return ans
            
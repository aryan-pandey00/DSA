class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: build prefix max
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
        
        # Step 2: traverse from right and track suffix min
        suffixMin = float('inf')
        ans = -1
        
        for i in range(n - 1, -1, -1):
            suffixMin = min(suffixMin, nums[i])
            
            if prefixMax[i] - suffixMin <= k:
                ans = i  # keep updating smallest index
        
        return ans
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: prefix max
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
        
        # Step 2: suffix min
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])
        
        # Step 3: find smallest stable index
        for i in range(n):
            if prefixMax[i] - suffixMin[i] <= k:
                return i
        
        return -1
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        left = 0
        total = sum(nums)  # Total sum of the array

        for i in range(len(nums)):
            
            # Exclude current element to get right sum
            right = total - left - nums[i]

            # Check if left and right sums are equal
            if left == right:
                return i

            left += nums[i]  # Add current element to left sum

        return -1  # No pivot index found
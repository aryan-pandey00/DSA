class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        max_ending = nums[0]
        min_ending = nums[0]
        result = abs(nums[0])

        for i in range(1, len(nums)):

            v1 = nums[i]  # Start new subarray
            v2 = max_ending + nums[i]  # Extend max subarray
            v3 = min_ending + nums[i]  # Extend min subarray

            # Best max/min sum ending here
            max_ending = max(v1, v2)
            min_ending = min(v1, v3)

            # Absolute value of max/min subarray
            ans1 = abs(max_ending)
            ans2 = abs(min_ending)

            # Update maximum absolute sum
            result = max(result, ans1, ans2)

        return result
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        max_ending = nums[0]
        min_ending = nums[0]
        result = nums[0]
        min_result = nums[0]

        total = sum(nums)  # total sum

        for i in range(1, len(nums)):

            v1 = nums[i]  # Start new subarray
            v2 = max_ending + nums[i]  # Extend max subarray
            v3 = min_ending + nums[i]  # Extend min subarray

            max_ending = max(v1, v2)
            min_ending = min(v1, v3)

            result = max(result, max_ending)
            min_result = min(min_result, min_ending)

        # All negative → circular sum is invalid
        if result < 0:
            return result

        sum2 = total - min_result  # Circular maximum

        return max(result, sum2)
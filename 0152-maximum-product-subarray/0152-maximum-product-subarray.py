class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_ending = nums[0]
        max_ending = nums[0]
        result = nums[0]

        for i in range (1,len(nums)):
            v1 = nums[i]  # Start a new subarray from current element
            v2 = min_ending * nums[i] # Extend min product
            v3 = max_ending * nums[i] # Extend max product

            # Maximum product ending at current position
            max_ending = max(v1, v2, v3)

            # Minimum product ending at current position
            min_ending = min(v1, v2, v3)

            # taking max as maximum product is asked otherwise can take min also
            result = max(result,max(max_ending,min_ending))

        return result
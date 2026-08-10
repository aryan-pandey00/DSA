class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0

        # j keeps moving and looks for non-zero
        # i points to the position where non-zero should go
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
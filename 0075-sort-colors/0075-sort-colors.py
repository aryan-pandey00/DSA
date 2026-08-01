class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            
            if nums[mid] == 0:
                # place 0 at correct position (left side)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # already in correct middle position
                mid += 1

            else:  # nums[mid] == 2
                # place 2 at correct position (right side)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # no need to move mid 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # sort array to apply two-pointer technique
        n = len(nums)
        
        diff = float('inf')  # stores minimum difference found so far
        res_sum = 0          # stores the closest sum corresponding to diff

        for i in range(n - 2):  # fix first element
            left = i + 1        # second element
            right = n - 1       # third element

            while left < right:
                total = nums[i] + nums[left] + nums[right]  
                d = abs(target - total)  # current difference from target
                
                # update result if we found a closer sum
                if diff > d: 
                    diff = d
                    res_sum = total  # update closest sum found so far

                # perfect match → cannot get better → exit early
                if total == target:
                    return res_sum

                # move pointers based on comparison
                if total < target:
                    left += 1   # need bigger sum
                else:
                    right -= 1  # need smaller sum

        return res_sum  
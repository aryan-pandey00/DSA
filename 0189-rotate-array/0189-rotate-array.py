class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k%len(nums) # this reduces the number of itteration 

        #reverse the whole array
        nums.reverse()

        #reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        #reverse remaining elements
        nums[k:] = reversed(nums[k:])
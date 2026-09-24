class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum = 0
        result = 0

        f = {0: 1}  # sum 0 exists once before the array starts

        for num in nums:
            sum += num

            ques = sum - k  # if this exists, remaining part = k

            result += f.get(ques, 0)  # add number of valid subarrays

            f[sum] = f.get(sum, 0) + 1  # remember this sum

        return result
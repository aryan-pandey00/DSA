class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        f = {}
        sum  = 0
        result = 0
        f[0] =1

        for i in range(len(nums)):

            sum += nums[i]
            rem = sum % k
            if rem < 0:
                rem = rem+k

            freq = f.get(rem,0)
            result += freq

            f[rem] = f.get(rem,0)+1

        return result 
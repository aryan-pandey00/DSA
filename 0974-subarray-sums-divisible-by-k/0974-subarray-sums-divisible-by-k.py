class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        f = {}
        sum = 0
        result = 0

        f[0] = 1  # remainder 0 exists once initially

        for i in range(len(nums)):
            sum += nums[i]

            rem = sum % k  # find remainder

            if rem < 0:
                rem += k  # make remainder positive

            freq = f.get(rem, 0)  # same remainder seen before 
            result += freq  # each gives a divisible subarray

            f[rem] = f.get(rem, 0) + 1  # store remainder in hashmap

        return result
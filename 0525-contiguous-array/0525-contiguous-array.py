class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        f = {}
        zero = 0
        one = 0
        result = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = one - zero

            if diff == 0:
                result = max(result, i + 1)# equal 0s & 1s from start, i+1 because strats from 0

            elif diff not in f:
                f[diff] = i  # remember first occurrence in hashmap

            else:
                length = i - f[diff]  # same diff → equal 0s & 1s
                result = max(result, length)

        return result
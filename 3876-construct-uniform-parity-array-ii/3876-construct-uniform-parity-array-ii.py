class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        nums1.sort()

        if nums1[0] % 2 == 1:
            return True

        return all(x % 2 == 0 for x in nums1)
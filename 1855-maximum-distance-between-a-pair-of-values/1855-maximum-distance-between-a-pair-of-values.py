class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        result = 0

        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                dist = j-i
                result = max(dist,result)
                j+=1

            else:
                i+=1

        return result
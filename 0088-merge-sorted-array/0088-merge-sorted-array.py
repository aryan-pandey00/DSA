class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # start from end of both array
        i = m-1 
        j = n-1
        k = m+n-1

        while i>=0 and j>=0:
            # bigger element go back at k 
            if nums1[i]>= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
                k-=1
            
            else:
                nums1[k] = nums2[j]
                j-=1
                k-=1
            
        while j>=0:
            # copy remaining n2 elements
            nums1[k] = nums2[j]
            j-=1
            k-=1
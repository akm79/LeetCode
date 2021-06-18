class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = nums1+nums2
        s=sorted(s)
        b=len(s)
        return (s[int(b/2)]+s[int((b-2)/2)])/2 if b%2==0 else  s[int(b/2)]

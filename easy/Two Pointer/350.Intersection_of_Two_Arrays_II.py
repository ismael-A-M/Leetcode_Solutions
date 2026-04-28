class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        l=0
        r=0
        s=[]
        while(l<len(nums1) and r<len(nums2)):
            if nums1[l]==nums2[r]:
                s.append(nums1[l])
                l+=1
                r+=1
            elif nums1[l]>nums2[r]:
                r+=1
            else:
                l+=1
        return s
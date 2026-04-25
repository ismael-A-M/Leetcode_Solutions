class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        h1=len(nums1)
        h2=len(nums2)
        c=h1+h2
        m=0
        k=0
        a=[]
        for i in range(c//2+1):
            if m<h2 and k<h1:
                if nums2[m]<=nums1[k]:
                    a.append(nums2[m])
                    m+=1
                else:
                    a.append(nums1[k])
                    k+=1

            elif m<h2:
                a.append(nums2[m])
                m+=1
            else:
                a.append(nums1[k])
                k+=1
        if c%2==0:
            return((a[-2]+a[-1])/2)
        else:
            return (a[-1])
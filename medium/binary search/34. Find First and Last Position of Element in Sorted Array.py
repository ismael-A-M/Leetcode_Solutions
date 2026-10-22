class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        t=len(nums)-1
        rannge = [-1,-1]
        left = 0
        right = t
        if nums==[]:
            return rannge

        while(left<=right):
            mid = (left+(right-left)//2)
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                rannge[0]=mid
                right=mid-1
        left = 0
        right = t
        while(left<=right):
            mid = (left+(right-left)//2)
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                rannge[1]=mid
                left=mid+1
        return rannge
                
                
                

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        k=0
        h=len(nums)-1
        for i in range(len(nums)):
            if nums[i]%2==0:
                l[k]=nums[i]
                k+=1
            else:
                l[h]=nums[i]
                h-=1
        return l
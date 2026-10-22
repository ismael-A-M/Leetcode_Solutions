class Solution:
    def canJump(self, nums: list[int]) -> bool:
        mx=nums[0]
        c=True
        for i in range(len(nums)-1):
            if nums[i]==0 and mx<=0:
                c=False
                break
            else:
                mx=max(nums[i],mx)
                mx-=1
        return c
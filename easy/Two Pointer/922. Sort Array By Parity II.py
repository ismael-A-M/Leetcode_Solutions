class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l,r=0,1
        while(True):
            while l<len(nums)  and nums[l]%2==0:
                l+=2
            while r<len(nums) and  nums[r]%2==1:
                r+=2
            if l>len(nums)or r>len(nums):
                break
            nums[l],nums[r]=nums[r],nums[l]
            l+=2 
            r+=2
        return nums
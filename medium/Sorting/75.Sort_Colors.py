class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for z in range(len(nums)-1-i):
                if nums[z]>nums[z+1]:
                    nums[z],nums[z+1]=nums[z+1],nums[z]
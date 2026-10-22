class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum=0
        max_sum= -10**5
        for i in range(len(nums)):
            current_sum+=nums[i]
            max_sum=max(current_sum,max_sum)
            if i<len(nums)-1 and current_sum<0 and current_sum<nums[i+1]:
                current_sum=0
        return max_sum
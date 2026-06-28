class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        SUM=sum(nums)
        left=0
        for i in range(len(nums)):
            right=SUM-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        else :
            return -1
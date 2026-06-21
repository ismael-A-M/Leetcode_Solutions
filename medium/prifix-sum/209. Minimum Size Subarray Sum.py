class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        c = 1
        MI = len(nums) + 1
        SUM = nums[l]

        while True:
            if SUM >= target:
                MI = min(c, MI)
                SUM -= nums[l]
                l += 1
                c -= 1
            else:
                r += 1
                if r >= len(nums):
                    break
                SUM += nums[r]
                c += 1
        if MI == len(nums) + 1:
            return 0  
        else:
            return MI
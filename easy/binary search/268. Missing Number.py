class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if mid < len(nums) and nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l
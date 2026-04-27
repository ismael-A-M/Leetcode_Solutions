class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val=False
        for i in range(len(nums)):
            if nums[i]==target:
                val=True
                ind=i
                break
        if val:
            return ind
        else:
            return -1

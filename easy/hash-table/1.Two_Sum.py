class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in check:
                return(check[val],i)
            check[nums[i]]=i
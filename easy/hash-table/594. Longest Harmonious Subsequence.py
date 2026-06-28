class Solution:
    def findLHS(self, nums: List[int]) -> int:
        arr=Counter(nums)
        c=0
        for i in arr:
            if i+1 in arr:
                c=max(arr[i]+arr[i+1],c)
        return c
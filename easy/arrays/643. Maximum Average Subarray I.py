class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        win=sum(nums[:k])
        mx=win
        for i in range(k,len(nums)):
            win-=nums[i-k]
            win+=nums[i]
            mx=max(mx,win)
        return(mx/k)
            

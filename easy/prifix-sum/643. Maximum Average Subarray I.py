class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        SUM=sum(nums[:k])
        VAV=SUM/k
        for i in range(len(nums)-k):
            SUM-=nums[i]
            SUM+=nums[k]
            VAV=max(VAV,SUM/k)
        return VAV
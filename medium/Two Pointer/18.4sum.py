class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        k=len(nums)
        li=[]
        for i in range(k-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,k-1):
                if nums[j]==nums[j-1] and j>i+1:
                    continue
                val=target-nums[i]-nums[j]
                l,r=j+1,k-1
                while (l<r):
                    n= nums[l]+nums[r]
                    if n==val:
                        li.append([nums[l],nums[r],nums[i],nums[j]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif n>val:
                        r-=1
                    else:
                        l+=1
        return li
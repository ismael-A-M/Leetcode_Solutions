class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k+=1
        arr=collections.Counter(nums[:k])
        c=False
        if arr.most_common(1)[0][1]>1:
            return True
        for i in range(len(nums)-k):
            arr[nums[i]]-=1
            if arr[nums[i]] == 0:
                del arr[nums[i]]
            if nums[i+k] in arr:
                c=True
                break
            else:
                arr[nums[i+k]]=1
        return c
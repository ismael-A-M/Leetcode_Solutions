class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        arr=Counter(nums)
        return(arr.most_common(1)[0][0])
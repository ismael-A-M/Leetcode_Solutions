class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        c=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            c=max(c,i-left+1)
        return c
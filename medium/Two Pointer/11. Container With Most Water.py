class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        mx=0
        while(l<r):
            c=min(height[l],height[r])
            w=r-l
            mx=max(c*w,mx)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return mx
class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while(l<=r):
            mid=(l+r)//2
            if mid*mid > x:
                r=mid-1
            elif mid*mid < x:
                l=mid+1
            else:
                break
        if mid*mid>x:
            return mid-1
        else:
            return mid
                        
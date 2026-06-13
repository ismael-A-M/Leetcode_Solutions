class Solution:
    def validPalindrome(self, s: str) -> bool:
        c=True
        n=len(s)
        l,r=0,n-1
        while(l<r):
            if s[l]!=s[r]:
                c=False
                break
            l+=1
            r-=1
        if c:
            return True
        l,r=0,n-1
        k=0
        c=True
        while(l<r):
            if s[l]!=s[r] and k==0:
                l+=1
                k=1
            if s[l]!=s[r]:
                c=False
                break
            l+=1
            r-=1
        if c:
            return True
        l,r=0,n-1
        k=0
        c=True
        while(l<r):
            if s[l]!=s[r] and k==0:
                r-=1
                k=1
            if s[l]!=s[r]:
                c=False
                break
            l+=1
            r-=1
        return c
            
        
        
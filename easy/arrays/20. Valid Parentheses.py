class Solution:
    def isValid(self, s: str) -> bool:
        l=0
        r=len(s)-1
        s=list(s)
        stack=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if stack[-1]=="(" and s[i]==")":
                    stack.pop(-1)
                elif stack[-1]=="[" and s[i]=="]":
                    stack.pop(-1)
                elif stack[-1]=="{" and s[i]=="}":
                    stack.pop(-1)
                else:
                    return(False)
        if not stack:
            return True
        else:
            return False
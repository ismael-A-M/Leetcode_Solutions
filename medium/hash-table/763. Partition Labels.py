class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l={}
        for i,ch in enumerate(s):
            l[ch]=i
        print(l)
        arr=[]
        ls=0
        r=0
        for i,ch in enumerate(s):
            ls=max(l[ch],ls)
            if ls==i:
                arr.append((i+1)-r)
                r=i+1
                ls=0
        return arr
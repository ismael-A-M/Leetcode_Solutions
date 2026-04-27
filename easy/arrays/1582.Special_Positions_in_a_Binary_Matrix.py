class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        l=[0]*len(mat[0])
        for i in range(len(mat)):
            if sum(mat[i])>1:
                for p in range(len(mat[0])):
                    if mat[i][p]==1:
                        l[p]=3
            for z in range(len(mat[0])):
                l[z]+=mat[i][z]
        return(l.count(1))

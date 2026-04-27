class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        column=len(dungeon[0])
        sol=[[0]*column for i in range(row)]
        if dungeon[-1][-1]>0:
            sol[-1][-1]=1
        else:
            sol[-1][-1]=1-dungeon[-1][-1]
        for i in range(row-2,-1,-1):
            sol[i][column-1]=max(sol[i+1][column-1]-dungeon[i][column-1],1)
        for i in range(column-2,-1,-1):
            sol[row-1][i]=max(sol[row-1][i+1]-dungeon[row-1][i],1)
        for i in range(row-2,-1,-1):
            for j in range(column-2,-1,-1):
                sol[i][j]=max(min(sol[i+1][j],sol[i][j+1])-dungeon[i][j],1)
        return sol[0][0]
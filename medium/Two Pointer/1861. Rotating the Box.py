class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for row in boxGrid:
            l = r = len(row) - 1

            while l >= 0:
                if row[l] == '*':
                    l -= 1
                    r = l
                elif row[l] == '#':
                    while r > l and row[r] != '.':
                        r -= 1

                    if r > l:
                        row[r], row[l] = row[l], '.'
                        r -= 1
                    else:
                        r = l - 1

                    l -= 1
                else:  # '.'
                    l -= 1

        BoxGrid = []
        for i in range(len(boxGrid[0])):
            col = []
            for z in range(len(boxGrid) - 1, -1, -1):
                col.append(boxGrid[z][i])
            BoxGrid.append(col)

        return BoxGrid
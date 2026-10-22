class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        s=len(matrix[0])-1
        while l<=r :

            mid=(l+r)//2

            if target<matrix[mid][0]:
                r=mid-1
            elif target>matrix[mid][-1]:
                l=mid+1
            else:
                break
        k=mid
        l=0
        r=s
        while l<=r:
            mid=(l+r)//2
            if target<matrix[k][mid]:
                r=mid-1
            elif target>matrix[k][mid]:
                l=mid+1
            else:
                return True
        return False

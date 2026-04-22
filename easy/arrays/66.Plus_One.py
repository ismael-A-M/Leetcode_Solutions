class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digt=list(str(int(''.join(map(str,digits)))+1))
        digt = [int(x) for x in digt]
        return(digt)    
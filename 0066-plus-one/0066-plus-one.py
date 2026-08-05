class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last=0
        for x in digits:
            last=last*10+x
        last=last+1
        res=[]
        for x in str(last):
            res.append(int(x))
        return res

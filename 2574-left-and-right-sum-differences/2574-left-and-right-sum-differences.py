class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        g=[]
        a,b=0,0
        for x in nums:
            a,b=b,b+x
            g.append(b)
        nums.reverse()
        h=[]
        a,b=0,0
        for x in nums:
            a,b=b,b+x
            h.append(b)
        h.reverse()
        z=[]
        for k,l in zip(g,h):
            y=abs(k-l)
            z.append(y)
        return z
    


        
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        a=[]
        b=[]
        for i in nums:
            if i>0:
                a.append(i)
            else:
                b.append(i)
        for k,l in zip(a,b):
            res.append(k)
            res.append(l)
        return res
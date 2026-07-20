class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            count=0
            f[i]=f.get(i,0)+1
            count+=1
        for k,v in f.items():
            if v==1:
                return k  
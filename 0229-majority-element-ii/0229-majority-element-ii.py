class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        print(n)
        h={}
        for i in nums:
            h[i]=h.get(i,0)+1
        print(h)
        l=[]
        for k,v in h.items():
            if v>n:
                l.append(k)
        return l
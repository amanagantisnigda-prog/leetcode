class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=min(nums)
        d=max(nums)
        for i in range(1,d+1):
            if s%i==0 and d%i==0:
                h=i
        return h
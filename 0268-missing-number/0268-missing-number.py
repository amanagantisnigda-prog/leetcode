class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # l=len(nums)
        # r=(l*(l+1))//2
        # sum=0
        # for i in nums:
        #     sum+=i
        # return r-sum
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i    
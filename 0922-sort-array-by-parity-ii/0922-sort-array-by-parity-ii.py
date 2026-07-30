class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
       n=[0]*len(nums)
       l=0
       m=1
       for i in nums:
            if i%2==0:
                n[l]=i
                l+=2
            else:
                n[m]=i
                m+=2
       return n



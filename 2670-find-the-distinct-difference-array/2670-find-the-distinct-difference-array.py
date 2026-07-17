class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            left=len(set(nums[:i+1]))
            right=len(set(nums[i+1:]))
            res.append(left-right)
        return res
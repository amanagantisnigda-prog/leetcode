class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            if i==len(nums)-k:
                return nums[i]

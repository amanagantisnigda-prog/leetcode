class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        l,r=0,len(nums)-1
        count=0
        while l<=r:
            if nums[l]==0 and nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                count+=1
                l+=1
                r-=1
            elif nums[l]!=0 and nums[r]!=0:
                l+=1
            elif nums[l]!=0 and nums[r]==0:
                r-=1
                l+=1
            else:
                r-=1
        return count


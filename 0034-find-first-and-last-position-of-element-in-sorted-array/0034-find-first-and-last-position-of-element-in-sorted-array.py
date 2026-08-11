class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low1,high1=0,len(nums)-1
        ans1=-1
        while(low1<=high1):
            mid=(low1+high1)//2
            if nums[mid]==target:
                ans1=mid
                high1=mid-1
            elif nums[mid]<target:
                low1=mid+1
            else:
                high1=mid-1
        low2,high2=0,len(nums)-1
        ans2=-1
        while(low2<=high2):
            mid=(low2+high2)//2
            if nums[mid]==target:
                ans2=mid
                low2=mid+1
            elif nums[mid]<target:
                low2=mid+1
            else:
                high2=mid-1
        return ans1,ans2
            
        
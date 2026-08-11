# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left,right=0,len(nums)-1
#         while(left<right):
#             mid=(left+right)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]>target:
#                 left=mid+1
#             elif nums[mid]<target:
#                 right=mid-1
#         return -1

                
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                return m
                
            elif nums[l]<=nums[m]:
                if nums[l]<=target and target<nums[m]:
                    r = m-1
                else:
                     l=m+1
            else:
                if nums[m]<target and target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
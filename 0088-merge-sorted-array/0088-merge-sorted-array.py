class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count=nums1.count(0)
        for i in range(n):
            nums1.remove(0)
        for i in nums2:
            nums1.append(i)
        return nums1.sort()

                
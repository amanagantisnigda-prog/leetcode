class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # for i in range(1,num//2):
        #     if (i*i)==num:
        #         return True
        #         break
        # else:
        #     return False
        n=int(num**0.5)
        return n*n==num
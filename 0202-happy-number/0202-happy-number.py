class Solution:
    def isHappy(self, n: int) -> bool:
        while n !=1 and n!=4:
            l=str(n)
            res=0
            for i in l:
                r=int(i)**2
                res+=r
            if res==n:
                return False
            n=res
        return n==1
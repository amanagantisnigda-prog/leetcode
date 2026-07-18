class Solution:
    def reverse(self, x: int) -> int:
        temp=abs(x)
        res=0
        l=len(str(temp))
        for y in range(l):
            last=temp%10
            res=res*10+last
            temp=temp//10
        if x<0: 
            res=-res
            # return res
        if res<-2**31 or res>2**31-1:
            return 0
        return res
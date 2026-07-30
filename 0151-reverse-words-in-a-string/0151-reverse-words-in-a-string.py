class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        print(d)
        l,r=0,len(d)-1
        while l<r:
            d[l],d[r]=d[r],d[l]
            l+=1
            r-=1
        return " ".join(d)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # r=s.split("-")
        # f=[i[::-1] for i in r]
        # g=f[::-1]
        # return ("-".join(g))
        s=list(s)
        l,r=0,len(s)-1
        a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        while l<r:
            if s[l] in a and s[r]  in a:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] not in a:
                l+=1
            else:
                r-=1
        return "".join(s)
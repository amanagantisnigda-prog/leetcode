class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l,r=0,len(s)-1
        u="aeiouAEIOU"
        while l<r:
            if s[l] in u and s[r] in u:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] not in u:
                l+=1
            elif s[r] not in u:
                r-=1
        return"".join(s)
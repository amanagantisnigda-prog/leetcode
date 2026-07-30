class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        k=len(s)-1
        i=0
        while i<=k:
            if s[i]==s[len(s)-1-i]:
                return i
            i+=1    
        return -1
               
        
class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()
        
        return " ".join(i[::-1]for i in t)
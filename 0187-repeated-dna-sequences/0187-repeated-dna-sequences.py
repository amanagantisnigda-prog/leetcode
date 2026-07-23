class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # d=[]
        f={}
        for i in range(len(s)-9):
            g=s[i:i+10]
            f[g]=f.get(g,0)+1
        # e=[]
        # for k,v in f.items():
        #     if v>1:
        #         e.append(k)
        return [k for k,v in f.items() if v>1]



        
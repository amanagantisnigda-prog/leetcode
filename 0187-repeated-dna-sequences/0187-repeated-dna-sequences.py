class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d=[]
        u=s
        for i in range(len(s)-9):
            g=u[i:i+10]
            d.append(g)
    
        f={}
        for j in d:
            f[j]=f.get(j,0)+1
        e=[]
        for k,v in f.items():
            if v>1:
                e.append(k)
        return e



        
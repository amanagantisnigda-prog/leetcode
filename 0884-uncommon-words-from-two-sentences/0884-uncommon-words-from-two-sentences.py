class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        p=s1.split()
        q=s2.split()
        g=p+q
        f={}
        for i in g:
            f[i]=f.get(i,0)+1
            # print(f)
        l=[]
        for k,v in f.items():
            if v==1:
                l.append(k)
        return(l)


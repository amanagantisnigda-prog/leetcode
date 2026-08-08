class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        g={}
        for i in words[0]:
            g[i]=g.get(i,0)+1
        # print(g)

        for i in words[1:]:
            u={}
            for p in i:
                u[p]=u.get(p,0)+1
            # print(u)
            # print(list(g.keys()))

            for i in list(g.keys()):
                if i in u:
                    g[i]=min(u[i],g[i])
                else:
                    del g[i]
        # print(g)
        result=[]
        for k,v in g.items():
            result.extend([k]*v)
        return result

            
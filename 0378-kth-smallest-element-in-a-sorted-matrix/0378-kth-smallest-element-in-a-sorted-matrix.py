class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        g=[]
        for i in matrix:
            if type(i)==list:
                for j in i:
                    g.append(j)
        print(len(g))
        g.sort()
        for u in range(len(g)):
            if (k-1)==u:
                return g[u]
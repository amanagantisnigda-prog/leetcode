class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def d_b(n):
            if type(n) not in [int, float, complex, bool]:
                return False
            n = int(n)   # ensure integer
            dv = ""
            while n != 0:
                j = n % 2
                dv = dv + str(j)
                n = n // 2
            return dv[::-1] if dv else "0"
        d = date.split("-") 
        res=[]
        for i in d:
            res.append(d_b(int(i)))
        return("-".join(res))


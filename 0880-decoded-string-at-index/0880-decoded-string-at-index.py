# class Solution:
#     def decodeAtIndex(self, s: str, k: int) -> str:
#         h=''
#         for i in s:
#             if 'a'<= i <= 'z':
#                 h+=i
#             elif '0' <= i <= '9':
#                 h*=int(i)
#         for i in range(len(h)):
#             if i==k:
#                 print(h[i-1])

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        # Pass 1: calculate the size of decoded string
        for i in s:
            if 'a' <= i <= 'z':
                size += 1
            elif '0' <= i <= '9':
                size *= int(i)
        
        # Pass 2: go backwards to find k-th char
        for i in s[::-1]:
            k %= size  # k wraps around
            if k == 0 and 'a' <= i <= 'z':
                return i
            if '0' <= i <= '9':
                size //= int(i)
            else:
                size -= 1
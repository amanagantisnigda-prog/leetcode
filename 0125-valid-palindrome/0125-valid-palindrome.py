# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         d=""
#         for i in s:
#             if i.isalnum():
#                 d+=i.lower()
#         if d==d[::-1]:
#             return True
#         return False


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-zA-Z0-9]','', s).lower()
        return result == result[::-1]
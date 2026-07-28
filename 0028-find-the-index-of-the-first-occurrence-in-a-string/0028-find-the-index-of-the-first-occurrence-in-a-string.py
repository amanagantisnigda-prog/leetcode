import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # res=re.search(needle,haystack)
        return haystack.find(needle)
        
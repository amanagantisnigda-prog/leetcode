class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string length
        min_len = len(strs[0])
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        
        prefix = ""
        
        # Compare characters one by one
        for i in range(min_len):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return prefix
            prefix += char
        
        return prefix
        
                
        
            

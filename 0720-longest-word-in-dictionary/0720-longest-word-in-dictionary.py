class Solution:
    def longestWord(self, words: List[str]) -> str:
        # g={}
        # for i in words:
        #     g[i]=len(i)
        # print(g)
        # l=0
        # for o in g:
        #     if g[o]>l:
        #         l=g[o] 
        # for d in g:
        #     if l==g[d]:
        #         return d


# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         wordSet = set(words) # for fast lookup
#         ans = ""
        
#         for word in words:
#             # check all prefixes exist: w, wo, wor, worl for "world"
#             valid = True
#             for i in range(1, len(word)):
#                 if word[:i] not in wordSet:
#                     valid = False
#                     break
            
#             if valid:
#                 # condition 1: longer
#                 # condition 2: same length but smaller lex order
#                 if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
#                     ans = word
#         return ans



        visited = set(words)
        result = ""
        for word in words:
            string = ""
            for w in word:
                string += w
                if string not in visited:
                    break
            else:
                if len(word) > len(result):
                    result = word
                elif len(word) == len(result):
                    result = min(result, word)
        return result
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=min(len(word1) ,len(word2))
        resp=""
        for i in range(n):
            resp +=word1[i]
            resp +=word2[i]
        resp += word1[n:]
        resp += word2[n:]
        return resp
            

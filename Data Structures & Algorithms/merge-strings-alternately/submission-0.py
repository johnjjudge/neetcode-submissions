class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        result = ""
        l = 0
        r = 0
        while l < len1 and r < len2:
            if l == r:
                result += word1[l]
                l+=1
            if l > r:
                result += word2[r]
                r+=1
        if l >= len1:
            for i in range(r, len2):
                result += word2[i]
        if r >= len2:
            for i in range(r, len1):
                result += word1[i]
        return result

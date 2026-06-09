class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDist = len(wordsDict)
        for l in range(len(wordsDict)):
            if wordsDict[l] == word1:
                r = l+1
                while r < len(wordsDict) and wordsDict[r] != word2:
                    r+=1
                if r < len(wordsDict) and wordsDict[r] == word2:
                    minDist = min(minDist, r-l)
            elif wordsDict[l] == word2:
                r = l+1
                while r < len(wordsDict) and wordsDict[r] != word1:
                    r+=1
                if r < len(wordsDict) and wordsDict[r] == word1:
                    minDist = min(minDist, r-l)
        return minDist

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        l = -1
        r = -1
        shortestDist = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                l = i
                if r > -1:
                    shortestDist = min(shortestDist, l-r)
            elif wordsDict[i] == word2:
                r = i
                if l > -1:
                    shortestDist = min(shortestDist, r-l)
        return shortestDist
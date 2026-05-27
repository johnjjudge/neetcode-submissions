class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = -1
        w2 = -1
        minDist = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
            elif wordsDict[i] == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                minDist = min(minDist, abs(w1 - w2))
        return minDist
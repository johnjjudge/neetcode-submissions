class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i = 0
        minDist = len(wordsDict)
        while i < len(wordsDict):
            if wordsDict[i] == word1:
                j = i + 1
                while j < len(wordsDict) and wordsDict[j] != word2:
                    j+=1
                if j < len(wordsDict):
                    minDist = min(minDist, j - i)

            elif wordsDict[i] == word2:
                j = i + 1
                while j < len(wordsDict) and wordsDict[j] != word1:
                    j+=1
                if j < len(wordsDict):
                    minDist = min(minDist, j - i)

            i+=1
        return minDist
        
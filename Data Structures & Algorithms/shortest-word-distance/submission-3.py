class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        words = {}
        words[word1] = []
        words[word2] = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                words[word1].append(i)
            elif wordsDict[i] == word2:
                words[word2].append(i)
        minDist = len(wordsDict)
        for i in words[word1]:
            for j in words[word2]:
                minDist = min(minDist, abs(i-j))

        return minDist

        
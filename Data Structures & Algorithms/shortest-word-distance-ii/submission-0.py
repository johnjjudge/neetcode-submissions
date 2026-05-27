class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.indexes = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.indexes:
                self.indexes[wordsDict[i]] = [i]
            else:
                self.indexes[wordsDict[i]].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        word1Indexes = self.indexes[word1]
        word2Indexes = self.indexes[word2]
        minDist = 3*10**4
        for i in range(len(word1Indexes)):
            for j in range(len(word2Indexes)):
                minDist = min(minDist, abs(word1Indexes[i]-word2Indexes[j]))
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

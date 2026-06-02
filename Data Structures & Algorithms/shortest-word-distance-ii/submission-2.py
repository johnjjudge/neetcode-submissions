class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDictLen = len(wordsDict)
        self.positions = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] in self.positions:
                self.positions[wordsDict[i]].append(i)
            else:
                self.positions[wordsDict[i]] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        minDist = self.wordsDictLen
        for word1Pos in self.positions[word1]:
            for word2Pos in self.positions[word2]:
                minDist = min(minDist, abs(word1Pos - word2Pos))

        return minDist
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.maxDist = len(wordsDict)
        self.words = defaultdict(list)
        for i in range(len(wordsDict)):
            self.words[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word1lst = self.words[word1]
        word2lst = self.words[word2]
        minDist = self.maxDist
        for pos1 in word1lst:
            for pos2 in word2lst:
                minDist = min(minDist, abs(pos1-pos2))
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

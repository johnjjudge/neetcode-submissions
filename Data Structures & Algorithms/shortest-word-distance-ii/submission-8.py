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
        i1,i2 = 0,0
        minDist = self.maxDist
        while i1 < len(word1lst) and i2 < len(word2lst):
            minDist = min(minDist, abs(word1lst[i1]-word2lst[i2]))
            if word1lst[i1] < word2lst[i2]:
                i1 += 1
            else:
                i2 += 1
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

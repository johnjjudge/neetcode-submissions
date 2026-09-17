class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.length = len(wordsDict)
        self.dic = defaultdict(list)
        for i in range(len(wordsDict)):
            self.dic[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        minNum = self.length
        for num1 in self.dic[word1]:
            for num2 in self.dic[word2]:
                minNum = min(abs(num1-num2), minNum)
        return minNum


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

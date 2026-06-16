class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.length = len(wordsDict)
        self.words = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.words:
                self.words[wordsDict[i]] = [i]
            else:
                self.words[wordsDict[i]].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        minNum = self.length
        for num1 in self.words[word1]:
            for num2 in self.words[word2]:
                minNum = min(abs(num1-num2), minNum)
        return minNum
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

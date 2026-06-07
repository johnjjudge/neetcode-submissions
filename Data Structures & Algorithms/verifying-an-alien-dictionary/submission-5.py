class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 0:
            return True
        orderDict = {}
        for i in range(len(order)):
            orderDict[order[i]] = i
        for i in range(len(words)-1):
            wordPtr = 0
            word1 = words[i]
            word2 = words[i+1]
            while True:
                if wordPtr >= len(word1):
                    break
                elif wordPtr < len(word1) and wordPtr >= len(word2):
                    return False
                elif orderDict[word1[wordPtr]] > orderDict[word2[wordPtr]]:
                    return False
                elif orderDict[word1[wordPtr]] < orderDict[word2[wordPtr]]:
                    break
                wordPtr += 1
                    
        return True


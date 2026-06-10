class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        orderDict = {}
        for i in range(len(order)):
            orderDict[order[i]] = i
        i = 0
        while i < len(words) - 1:
            word1 = words[i]
            word2 = words[i+1]
            wordPtr = 0
            
            while wordPtr < len(word1):
                if wordPtr >= len(word2):
                    return False
                elif orderDict[word1[wordPtr]] < orderDict[word2[wordPtr]]:
                    break
                elif orderDict[word1[wordPtr]] > orderDict[word2[wordPtr]]:
                    return False
                wordPtr +=1
            i += 1
        return True
                
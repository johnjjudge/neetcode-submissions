class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {}
        for i in range(len(order)):
            orders[order[i]] = i

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for i in range(len(word1)):
                if i == len(word2):
                    return False
                if orders[word1[i]] > orders[word2[i]]:
                    return False
                if orders[word1[i]] < orders[word2[i]]:
                    break
                i+=1
        return True
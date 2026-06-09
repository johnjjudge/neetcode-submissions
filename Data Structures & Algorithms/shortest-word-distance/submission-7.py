class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = float('inf')
        i2 = float('-inf')
        res = float('inf')

        for i, w in enumerate(wordsDict):
            if w == word1:
                i1 = i
            elif w == word2:
                i2 = i
            res = min(res, abs(i2 - i1))

        return res
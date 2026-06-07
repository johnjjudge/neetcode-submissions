class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}
        sortedWords = sorted(words, key=lambda word: [rank[ch] for ch in word])
        if sortedWords != words:
            return False
        return True

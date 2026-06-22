class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        i = 0
        common = Counter(words[i])
        while i < len(words):
            common = common & Counter(words[i])
            i+=1
        return list(common.elements())
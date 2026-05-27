class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common = 201
        for s in range(len(strs)-1):
            firstWord = strs[s]
            secondWord = strs[s+1]
            j = 0
            while j < len(firstWord) and j < len(secondWord) and firstWord[j] == secondWord[j]:
                j+=1
            common = min(common, j)
        s = ""
        for i in range(common):
            s += strs[0][i]
        return s

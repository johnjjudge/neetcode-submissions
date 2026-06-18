class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr in anagrams:
                anagrams[sortedStr].append(strs[i])
            else:
                anagrams[sortedStr] = [strs[i]]
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        return result
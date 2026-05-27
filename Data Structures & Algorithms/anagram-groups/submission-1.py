class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            sortedChars = ''.join(sorted(strs[i]))
            if sortedChars not in anagrams:
                anagrams[sortedChars] = [strs[i]]
            else:
                anagrams[sortedChars].append(strs[i])
        result = []
        for kv in anagrams:
            result.append(anagrams[kv])
        return result
        
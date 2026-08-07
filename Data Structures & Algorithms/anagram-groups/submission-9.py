class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in anagrams:
                anagrams[sortedS].append(s)
            else:
                anagrams[sortedS] = [s]
        for a in anagrams:
            result.append(anagrams[a])
        return result
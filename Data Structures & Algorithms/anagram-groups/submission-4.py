class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}
        for word in strs:
            sort = ''.join(sorted(word))
            if sort in anagrams:
                anagrams[sort].append(word)
            else:
                anagrams[sort] = [word]

        for key in anagrams:
            result.append(anagrams[key])
        return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            wordSorted = ''.join(sorted(word))
            if wordSorted in anagrams:
                anagrams[wordSorted].append(word)
            else:
                anagrams[wordSorted] = [word]
        
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        return result
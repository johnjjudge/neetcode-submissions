class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charsInS = {}
        for char in s:
            if char in charsInS:
                charsInS[char] += 1
            else:
                charsInS[char] = 1     

        for char in t:
            if char in charsInS:
                charsInS[char] -= 1
            else:
                return False

        for i in charsInS:
            if charsInS[i] != 0:
                return False
        
        return True


        
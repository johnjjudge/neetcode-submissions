class Solution:
    def countSubstrings(self, s: str) -> int:
        lenS = len(s)
        num = 0
        for i in range(lenS):
            num += 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < lenS and s[l] == s[r]:
                num +=1
                l-=1
                r+=1
            l = i
            r = i + 1
            while l >= 0 and r < lenS and s[l] == s[r]:
                num +=1
                l-=1
                r+=1
        return num
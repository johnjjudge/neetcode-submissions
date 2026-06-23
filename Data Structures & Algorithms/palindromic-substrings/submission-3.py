class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l-=1
                r+=1
            r = i + 1
            l = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l-=1
                r+=1
            count+=1
            i +=1
        return count
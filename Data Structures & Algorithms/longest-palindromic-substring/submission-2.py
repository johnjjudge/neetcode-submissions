class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxPalLen = 1
        maxPal = s[0]
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                palLen = 0
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    palLen = r - l + 1
                    if palLen > maxPalLen:
                        maxPalLen = palLen
                        maxPal = s[l:r+1]
                    l -= 1
                    r += 1
        return maxPal
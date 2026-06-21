class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]] = 1
            else:
                counts[s[i]] += 1
        result = 0
        has_odd = False
        for key in counts:
            if counts[key] % 2 == 0:
                result += counts[key]
            else:
                result += counts[key] - 1
                has_odd = True
        return result + 1 if has_odd else result
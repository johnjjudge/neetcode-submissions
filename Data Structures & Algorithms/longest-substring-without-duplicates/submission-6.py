class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        chars = set()
        r = 0
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                maxLength = max(maxLength, r - l)
            else:
                chars.remove(s[l])
                l += 1
        return maxLength
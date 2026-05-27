class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxSubstring = 0
        for left in range(len(s)):
            seen = set()
            seen.add(s[left])
            right = left+1
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right+=1
            maxSubstring = max(maxSubstring, right - left)
        return maxSubstring

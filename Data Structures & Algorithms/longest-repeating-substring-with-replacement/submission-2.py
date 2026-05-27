class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        maxLen = 0
        for left in range(len(s)):
            right = left + 1
            numReplace = k
            while right < len(s):
                if s[right] == s[left]:
                    right += 1
                else:
                    if numReplace == 0:
                        break
                    else:
                        numReplace -= 1
                        right += 1
            if numReplace == 0:
                maxLen = max(maxLen, right - left)
            else:
                maxLen = max(maxLen, min(right - left + numReplace, len(s)))
        return maxLen
        
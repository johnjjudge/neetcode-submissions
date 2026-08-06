class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        longest = 0
        atLeastOneOdd = False
        for i in counts:
            if counts[i] % 2 == 1:
                longest += counts[i] - 1
                atLeastOneOdd = True
            else:
                longest += counts[i]
        if atLeastOneOdd:
            return longest + 1
        return longest

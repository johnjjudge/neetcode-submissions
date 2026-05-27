class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lens = len(s)
        half = lens//2
        for i in range(half):
            tmp = s[lens-1-i]
            s[lens-1-i] = s[i]
            s[i] = tmp
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        l = 0
        r = len(xStr)-1
        while l < r:
            if xStr[l] != xStr[r]:
                return False
            l += 1
            r -= 1
        return True
        
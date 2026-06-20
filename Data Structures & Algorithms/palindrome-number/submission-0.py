class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        l = 0
        r = len(strX) - 1
        while l < r:
            if strX[l] != strX[r]:
                return False
            l += 1
            r -=1
        return True
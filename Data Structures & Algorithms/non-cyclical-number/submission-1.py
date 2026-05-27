class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            num = 0
            for digit in str(n):
                num += int(digit)**2

            n = num
        return True




        
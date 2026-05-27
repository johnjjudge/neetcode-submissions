class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = sign * int(str(x_abs)[::-1])

        if reversed_x > 2**31 -1 or reversed_x < -2**31:
            return 0
        return reversed_x
        
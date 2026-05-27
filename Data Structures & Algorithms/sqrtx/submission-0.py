class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 0
        r = x
        while l <= r:
            m = l + (r-l)//2
            if m*m == x:
                return m
            elif m*m < x:
                if (m+1)*(m+1) > x:
                    return m
                l = m + 1
            elif m*m > x:
                if (m-1)*(m-1) < x:
                    return m-1
                r = m - 1
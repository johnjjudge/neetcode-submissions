class Solution:
    def climbStairs(self, n: int) -> int:
        #f(0) = 0 .. not necessary but for explination
        #f(1) = 1
        #f(2) = 2
        #f(n) = f(n-1) + f(n-2) + ... + f(2) + f(1)
        if n <= 2:
            return n
        dp = [1, 2]
        i = 2
        while i < n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]


        
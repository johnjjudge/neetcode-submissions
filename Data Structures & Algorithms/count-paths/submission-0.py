class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1:
            return 1

        rowBelow = [1]*n

        for r in range(m-2,-1, -1):
            rowAbove = [0]*n
            rowAbove[n-1] = 1
            for c in range(n-2,-1,-1):
                rowAbove[c] = rowAbove[c+1] + rowBelow[c]
            rowBelow = rowAbove
        return rowBelow[0]

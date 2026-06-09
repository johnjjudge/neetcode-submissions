class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        numRows = len(grid)
        numCols = len(grid[0])
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    islands.add(self.island(grid, r, c, "S"))
        return len(islands)

    def island(self, grid, r, c, direction):
        if r < 0 or r >= len(grid) or c < 0 or c >=len(grid[r]) or grid[r][c] != 1:
            return ""
        
        grid[r][c] = -1
        direction += self.island(grid, r+1, c, "D")
        direction += self.island(grid, r, c+1, "R")
        direction += self.island(grid, r, c-1, "L")
        direction += self.island(grid, r-1, c, "U")
        direction += "E"
        return direction
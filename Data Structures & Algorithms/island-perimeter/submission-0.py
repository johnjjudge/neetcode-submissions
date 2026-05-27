class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    for d in dirs:
                        newR = r + d[0]
                        newC = c + d[1]
                        if newR == len(grid) or newR < 0 or grid[newR][c] == 0:
                            p += 1
                        if newC == len(grid[0]) or newC < 0 or grid[r][newC] == 0:
                            p += 1
        return p
                        

        
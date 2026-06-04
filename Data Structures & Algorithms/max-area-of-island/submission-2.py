class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islandNum = -1
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        maxArea = 0
        numRows = len(grid)
        numCols = len(grid[0])

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    def bfs(r: int, c: int):
                        islandSize = 0
                        queue = deque()
                        queue.append((r,c))
                        grid[r][c] = islandNum
                        while len(queue) > 0:
                            cr, cc = queue.popleft()
                            islandSize += 1
                            for dr, dc in dirs:
                                nr = cr + dr
                                nc = cc + dc
                                if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == 1:
                                    grid[nr][nc] = islandNum
                                    queue.append((nr,nc))

                        return islandSize
                    islandNum -= 1 
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea
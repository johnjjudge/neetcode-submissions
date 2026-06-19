class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        numRows = len(grid)
        numCols = len(grid[0])

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    numIslands -=1
                    def bfs(r,c):
                        queue = deque()
                        queue.append((r,c))
                        grid[r][c] == str(numIslands)
                        while len(queue) > 0:
                            cordX,cordY = queue.popleft()
                            for d in dirs:
                                newX = d[0] + cordX
                                newY = d[1] + cordY
                                if 0 <= newX < numRows and 0 <= newY < numCols and grid[newX][newY] == "1":
                                    grid[newX][newY] = str(numIslands)
                                    queue.append((newX, newY))
                    bfs(r,c)
        return numIslands * -1

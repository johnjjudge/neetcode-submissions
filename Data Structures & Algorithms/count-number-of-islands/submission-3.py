class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        numIslands = 0
        queue = deque()

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    queue.append((r,c))
                    def bfs():
                        r,c = queue.popleft()
                        for nr, nc in dirs:
                            newR = nr + r
                            newC = nc + c
                            if 0 <= newR < numRows and 0 <= newC < numCols and grid[r][c] == "1":
                                queue.append((newR, newC))
                        grid[r][c] = "X"
                    while len(queue) > 0:
                        bfs()
                    numIslands +=1
        return numIslands
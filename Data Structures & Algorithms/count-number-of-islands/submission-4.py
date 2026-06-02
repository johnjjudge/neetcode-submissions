class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numToUse = -1
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        numRows = len(grid)
        numCols = len(grid[0])

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    
                    def bfs(r: int, c: int):
                        queue = deque()
                        queue.append((r,c))
                        while len(queue) > 0:
                            cordR,cordC = queue.popleft()
                            for newR, newC in dirs:
                                x = cordR + newR
                                y = cordC + newC
                                if 0 <= x < numRows and 0 <= y < numCols and grid[x][y] == "1":
                                    queue.append((x,y))
                            grid[cordR][cordC] = str(numToUse)
                    bfs(r,c)
                    numToUse -= 1


        return abs(numToUse) - 1
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])

        numIslands = 0

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    def bfs(r: int, c: int):
                        queue = deque()
                        queue.append((r,c))
                        grid[r][c] = "-1"
                        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
                        while len(queue) > 0:
                            pr, pc = queue.popleft()

                            for d in dirs:
                                nr = pr + d[0]
                                nc = pc + d[1]
                                if 0<=nr<numRows and 0<=nc<numCols and grid[nr][nc] == "1":
                                    grid[nr][nc] = "-1"
                                    queue.append((nr, nc))
                            
                    bfs(r, c)
                    numIslands+=1
        return numIslands


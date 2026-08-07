class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        numRows = len(grid)
        numCols = len(grid[0])
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == '1':
                    def bfs(r: int, c: int):
                        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                        queue = deque()
                        grid[r][c] = '0'
                        queue.append((r,c))
                        while len(queue) > 0:
                            pr, pc = queue.popleft()
                            for dr, dc in dirs:
                                nr = pr + dr
                                nc = pc + dc
                                if 0 <= nr < numRows and 0<= nc < numCols and grid[nr][nc] == '1':
                                    grid[nr][nc] = '0'
                                    queue.append((nr,nc))
                    bfs(r, c)
                    numIslands += 1
        return numIslands
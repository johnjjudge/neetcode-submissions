class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])

        if grid[0][0] != 0 or grid[numRows-1][numCols-1] != 0:
            return -1
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]
        queue = deque()
        queue.append((0,0,1))
        while len(queue) > 0:
            r,c,n = queue.popleft()
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == 0:
                    if nr == numRows - 1 and nc == numCols -1:
                        return n + 1
                    queue.append((nr,nc,n+1))
                    grid[nr][nc] = -1
        return -1
                
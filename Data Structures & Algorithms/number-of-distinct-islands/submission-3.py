class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        islands = set()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    def bfs(r: int, c: int):
                        island = [(0,0)]
                        queue = deque()
                        queue.append((r,c))
                        grid[r][c] = -1
                        while len(queue) > 0:
                            pr,pc = queue.popleft()
                            for dr, dc in dirs:
                                nr = pr + dr
                                nc = pc + dc
                                if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == 1:
                                    queue.append((nr,nc))
                                    grid[nr][nc] = -1
                                    island.append((r-nr,c-nc))
                        return island
                    islands.add(frozenset(bfs(r,c)))

        return len(islands)
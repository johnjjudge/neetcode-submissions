class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        islandsSets = set()
        numRows = len(grid)
        numCols = len(grid[0])

        for row in range(numRows):
            for col in range(numCols):
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                if grid[row][col] == 1:
                    islandSet = {(0, 0)}
                    islands = self.bfs(row, col, row, col, numRows, numCols, seen, grid, islandSet)
                    islandsSets.add(tuple(islands))
        return len(islandsSets)

    def bfs(self, initialRow: int, initialCol: int, row: int, col: int, numRows: int, numCols: int, seen: set, grid: List[List[int]], islandSet: set):
        queue = deque([(row, col)])
        while len(queue) > 0:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < numRows and 0 <= nc < numCols and (nr, nc) not in seen and grid[nr][nc] == 1:
                    seen.add((nr, nc))
                    islandSet.add((nr - initialRow, nc - initialCol))
                    queue.append((nr, nc))

        return islandSet

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        numIslands = 0
        numRows = len(grid)
        numCols = len(grid[0])

        for row in range(numRows):
            for col in range(numCols):
                if (row, col) not in seen and grid[row][col] == "1":
                    numIslands += 1
                    seen.add((row, col))
                    self.bfs((row, col), grid, seen, numRows, numCols)
                if (row, col) not in seen and grid[row][col] == "0":
                    seen.add((row, col))
        
        return numIslands

    def bfs(self, cord: tuple, grid: List[List[str]], seen: set, numRows: int, numCols: int):
        queue = deque()
        queue.append(cord)
        while len(queue) > 0:
            checkCord = queue.popleft()
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for i in range(len(dirs)):
                newCordX = checkCord[0] + dirs[i][0]
                newCordY = checkCord[1] + dirs[i][1]
                if 0 <= newCordX < numRows and 0 <= newCordY < numCols and (newCordX, newCordY) not in seen:
                    seen.add((newCordX, newCordY))
                    if grid[newCordX][newCordY] == "1":
                        queue.append((newCordX, newCordY))
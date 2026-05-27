class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0:
            return -1
        
        path = self.bfs(grid)
        if path == None:
            return -1
        else:
            return path
        
    def bfs(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        queue = deque()
        visited = set()
        shortestPath = 1

        queue.append((0,0))
        visited.add((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == numRows - 1 and c == numCols -1:
                    return shortestPath


                directions = [[1,0], [-1,0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr == numRows or c + dc == numCols or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1):
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            shortestPath += 1
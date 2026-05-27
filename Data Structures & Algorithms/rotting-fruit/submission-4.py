class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1


        numRows = len(grid)
        numCols = len(grid[0])

        queue = deque()
        visited = set()
        shortestPath = 0
        numFresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    numFresh +=1

        while queue and numFresh > 0:
            shortestPath += 1
            for i in range(len(queue)):
                r, c = queue.popleft()

                directions = [[1,0], [-1,0], [0,-1], [0,1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        numFresh -=1
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                    
                


        if numFresh > 0:
            return -1
        else:
            return shortestPath
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        cols, rows = len(grid[0]), len(grid)

        max_area = 0

        visited = set()

        def get_area(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            # The area is 1 (current) + area of all neighbors
            return 1 + get_area(r+1, c) + get_area(r-1, c) + get_area(r, c+1) + get_area(r, c-1)


        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1 :
                    size_of_island = get_area(i,j)
                    max_area = max(max_area, size_of_island)
                    
                    
        
        return max_area
        
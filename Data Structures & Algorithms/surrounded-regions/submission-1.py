class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numRows = len(board)
        numCols = len(board[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()

        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    def bfs(start_r: int, start_c: int):
                        touchesEdge = False
                        island = set()
                        queue = deque()
                        queue.append((start_r,start_c))
                        island.add((start_r,start_c))
                        visited.add((start_r,start_c))
                        while len(queue) > 0:
                            cr, cc = queue.popleft()
                            if cr == 0 or cc == 0 or cc == numCols - 1 or cr == numRows - 1:
                                touchesEdge = True
                            for dr, dc in dirs:
                                nr = cr + dr
                                nc = cc + dc
                                if 0 <= nr < numRows and 0 <= nc < numCols and board[nr][nc] == 'O' and (nr, nc) not in island:
                                    queue.append((nr,nc))
                                    island.add((nr,nc))
                                    visited.add((nr,nc))
                        if not touchesEdge:
                            for cordR, cordC in island:
                                board[cordR][cordC] = 'X'
                    bfs(r,c)

        


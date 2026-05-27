class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Iterate board and update set to say where we visited
        # Find Os
        # BFS to find all attached Os. Add them to list instead of queue and update counter to next
        # If we go through every direction and do not hit an edge then set all cords in list to X
        seen = set()
        numRows = len(board)
        numCols = len(board[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        for r in range(numRows):
            for c in range(numCols):
                if (r,c) in seen:
                    continue

                elif board[r][c] == 'O':
                    toFlip = deque()
                    toFlip.append((r,c))
                    bfsQ = deque()
                    bfsQ.append((r,c))
                    seen.add((r,c))
                    hitEdge = False
                    while len(bfsQ) > 0:
                        def bfs():
                            nonlocal hitEdge
                            r, c = bfsQ.popleft()
                            if r == 0 or r == numRows - 1 or c == 0 or c == numCols - 1:
                                hitEdge = True
                            for d in dirs:
                                nr = d[0] + r
                                nc = d[1] + c
                                if 0 <= nr < numRows and 0 <= nc < numCols and board[nr][nc] == 'O' and (nr, nc) not in seen:
                                    seen.add((nr, nc))
                                    bfsQ.append((nr, nc))
                                    toFlip.append((nr, nc))

                        bfs()
                        
                    if hitEdge == False:
                        while len(toFlip) > 0:
                            fr, fc = toFlip.popleft()
                            board[fr][fc] = 'X'

                elif board[r][c] == 'X':
                    seen.add((r,c))

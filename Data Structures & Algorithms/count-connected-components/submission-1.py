class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        numComp = 0
        for c in graph:
            def bfs(c: int):
                if c in visited:
                    return 0
                visited.add(c)
                queue = deque([c])
                while len(queue) > 0:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                return 1
                    
            numComp += bfs(c)
        return numComp

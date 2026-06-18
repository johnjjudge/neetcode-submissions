class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPreqs = [0]*numCourses
        graph = [set() for _ in range(numCourses)]
        for combo in prerequisites:
            graph[combo[1]].add(combo[0])
            numPreqs[combo[0]] += 1
        
        coursesTaken = 0
        queue = deque()
        for i in range(len(numPreqs)):
            if numPreqs[i] == 0:
                queue.append(i)
                coursesTaken +=1

        while len(queue) > 0:
            course = queue.popleft()
            for neighbor in graph[course]:
                numPreqs[neighbor]-=1
                if numPreqs[neighbor] == 0:
                    queue.append(neighbor)
                    coursesTaken += 1
        return coursesTaken == numCourses

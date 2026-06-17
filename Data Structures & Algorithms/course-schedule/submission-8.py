class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create numPreqs which has counts of the number of prereqs each course (i) has
        numPreqs = [0] * numCourses
        # Create adjacency list of all prereqs a course (i) has
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            numPreqs[dst] += 1
            adj[src].append(dst)

        # Add all courses which have no prereqs to a queue
        queue = deque()
        for n in range(numCourses):
            if numPreqs[n] == 0:
                queue.append(n)

        # While the queue is not empty
        # Pop elem, mark it as taken (increment taken counter)
        # Reduce the number of prereqs for courses which is it a prereq for
        # If any of those courses no longer have a prereq count, add them to the queue
        taken = 0
        while queue:
            node = queue.popleft()
            taken += 1
            for nei in adj[node]:
                numPreqs[nei] -= 1
                if numPreqs[nei] == 0:
                    queue.append(nei)

        # Since we incremented the counter for every course we took, if numCourses != taken,
        # then we should return false because there was some course we could not take
        return taken == numCourses
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # The problem asks us to detect if there are any cycles in the graph
        # A cycle being a 0 -> 1, 1 -> 0 or similar
        # So to solve this problem first lets construct the graph using a dict
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for c,p in prerequisites:
            graph[p].append(c)
        
        
        visited = set() # to keep track of courses we have fully processed
        in_stack = set() # to keep track of courses on a single dfs dive

        def dfs(course):
            # returns true if a cycle is detected
            
            visited.add(course) # we are going to process this course
            in_stack.add(course) # we are in the middle of processing this course

            for neighbor in graph[course]: # check every course this is a prereq for
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True #propogate True up the call-stack
                elif neighbor in in_stack:
                    return True #a cycle has been detected
            
            in_stack.remove(course) # we are done processing this cource
            return False #Nothing says we can't finish this course so say no cycle detected

        for course in range(numCourses): # go through all the courses
            if course not in visited: # if we have not already processed them
                if dfs(course): # do a dfs dive to make sure we can complete the course
                    return False # return false if we can't

        # Nothing says we can't complete the courses so return true
        return True 